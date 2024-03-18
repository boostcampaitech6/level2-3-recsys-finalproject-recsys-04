import torch
import torch.nn as nn
import numpy as np

from .module import BERT4RecBlock

params = {
    "max_len":20,
    "hidden_units":50,
    "num_heads":1,
    "num_layers":2,
    "dropout_rate":0.5,
    "num_item":8587,
    "device":'cuda',
}

# model setting
class BERT4Rec(nn.Module):
    def __init__(self, **params):
        super(BERT4Rec, self).__init__()
        
        self.num_item = params["num_item"]
        self.hidden_units = params["hidden_units"]
        self.num_heads = params["num_heads"]
        self.num_layers = params["num_layers"]
        self.max_len = params["max_len"]
        self.dropout_rate = params["dropout_rate"]
        self.device = params["device"]

        self.item_emb = nn.Embedding(self.num_item + 2, self.hidden_units, padding_idx=0) # TODO2: mask와 padding을 고려하여 embedding을 생성해보세요.
        self.pos_emb = nn.Embedding(self.max_len, self.hidden_units) # learnable positional encoding
        self.dropout = nn.Dropout(self.dropout_rate)
        self.emb_layernorm = nn.LayerNorm(self.hidden_units, eps=1e-6)

        self.blocks = nn.ModuleList([BERT4RecBlock(self.num_heads, self.hidden_units, self.dropout_rate) for _ in range(self.num_layers)])
        self.out = nn.Linear(self.hidden_units, self.num_item + 1) # TODO3: 예측을 위한 output layer를 구현해보세요. (num_item 주의)

    def forward(self, log_seqs):
        seqs = self.item_emb(torch.LongTensor(log_seqs).to(self.device))
        positions = np.tile(np.array(range(log_seqs.shape[1])), [log_seqs.shape[0], 1])
        seqs += self.pos_emb(torch.LongTensor(positions).to(self.device))
        seqs = self.emb_layernorm(self.dropout(seqs))

        mask = torch.BoolTensor(log_seqs > 0).unsqueeze(1).repeat(1, log_seqs.shape[1], 1).unsqueeze(1).to(self.device) # mask for zero pad
        for block in self.blocks:
            seqs, attn_dist = block(seqs, mask)
        out = self.out(seqs)
        return out