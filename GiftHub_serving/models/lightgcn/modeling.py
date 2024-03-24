# modeling.py
import torch
import torch.nn as nn
import torch.nn.functional as F
from torch.utils.data import DataLoader, Dataset
import numpy as np

class LightGCN(nn.Module):
    def __init__(self, n_users, n_items, emb_dim, n_layers, reg, adj_mtx, device):
        super(LightGCN, self).__init__()
        self.n_users = n_users
        self.n_items = n_items
        self.emb_dim = emb_dim
        self.n_layers = n_layers
        self.reg = reg
        self.device = device
        self.user_embedding = nn.Embedding(n_users, emb_dim).to(device)
        self.item_embedding = nn.Embedding(n_items, emb_dim).to(device)
        nn.init.normal_(self.user_embedding.weight, std=0.1)
        nn.init.normal_(self.item_embedding.weight, std=0.1)
        self.adj_mtx = self._convert_sp_mat_to_sp_tensor(adj_mtx).to(device)

    def _convert_sp_mat_to_sp_tensor(self, X):
        coo = X.tocoo().astype(np.float32)
        i = torch.LongTensor(np.mat([coo.row, coo.col]))
        v = torch.FloatTensor(coo.data)
        return torch.sparse.FloatTensor(i, v, coo.shape).to(self.device)

    def forward(self, users, pos_items, neg_items):
        all_embeddings = self.compute_embeddings()
        u_embeddings = all_embeddings[:self.n_users]
        i_embeddings = all_embeddings[self.n_users:]
        users_emb = u_embeddings[users]
        pos_emb = i_embeddings[pos_items]
        neg_emb = i_embeddings[neg_items]
        pos_scores = torch.sum(users_emb * pos_emb, dim=-1)
        neg_scores = torch.sum(users_emb * neg_emb, dim=-1)
        loss = -torch.mean(F.logsigmoid(pos_scores - neg_scores))
        if self.reg > 0:
            reg_term = (1/2)*(users_emb.norm(2).pow(2) + 
                              pos_emb.norm(2).pow(2) + 
                              neg_emb.norm(2).pow(2))/float(len(users))
            loss += self.reg * reg_term
        return loss

    def compute_embeddings(self):
        users_emb = self.user_embedding.weight
        items_emb = self.item_embedding.weight
        all_emb = torch.cat([users_emb, items_emb])
        embs = [all_emb]
        for _ in range(self.n_layers):
            all_emb = torch.sparse.mm(self.adj_mtx, all_emb)
            embs.append(all_emb)
        embs = torch.stack(embs, dim=1)
        light_out = torch.mean(embs, dim=1)
        return light_out


