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
    return session_item_embeddings, item_embeddings, user_embeddings

def recommend_item(session_user_embedding, item_embeddings, top_k):
    scores = torch.matmul(session_user_embedding, item_embeddings.T)
    top_scores, top_indices = torch.topk(scores, k=top_k, dim=1)
    return top_indices.squeeze().tolist()


def recommend_users(session_item_embeddings, user_embeddings, top_k):
    # 세션 사용자 임베딩과 모든 사용자 임베딩 간의 유사도를 계산
    scores = torch.matmul(session_item_embeddings, user_embeddings.T)
    top_scores, top_indices = torch.topk(scores, k=top_k, dim=1)
    return top_indices.squeeze().tolist()

def random_item(recommended_user_ids, data, k) : 
    # 유사한 사용자의 아이템 추천 받기
    total_items = []
    for user_id in recommended_user_ids:
        # 여기서는 'product_id' 대신 실제 data에서 사용하는 상호작용 아이템 컬럼명을 사용하세요.
        user_items = data[data['user_id'] == user_id]['product_id'].tolist()
        total_items.extend(user_items)


    # 고유 아이템 선택
    unique_items = list(set(total_items))

    recommended_items = random.sample(unique_items, k) if len(unique_items) >= k else unique_items
    return print(recommended_items[:10])