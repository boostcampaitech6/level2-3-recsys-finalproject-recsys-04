# recommend.py
import torch
import numpy as np
import random

def load_model(model_path, model, device):
    model.load_state_dict(torch.load(model_path, map_location=device))
    model.eval()
    return model

def encode_session_items(preprocess, session_items):
    encoded_items = [preprocess.item_encoder[item] for item in session_items if item in preprocess.item_encoder]
    return encoded_items

def infer_embeddings(model, encoded_session_items, num_users, num_items, device):
    with torch.no_grad():
        all_embeddings = model.compute_embeddings()
        user_embeddings = all_embeddings[:num_users]
        item_embeddings = all_embeddings[num_users:]

        if encoded_session_items:
            session_item_embeddings = item_embeddings[encoded_session_items].mean(dim=0).unsqueeze(0)
        else:
            session_item_embeddings = user_embeddings[torch.randint(0, num_users, (1,))]
    return session_item_embeddings, item_embeddings

def recommend_item(session_user_embedding, item_embeddings, top_k):
    scores = torch.matmul(session_user_embedding, item_embeddings.T)
    top_scores, top_indices = torch.topk(scores, k=top_k, dim=1)
    return top_indices.squeeze().tolist()

