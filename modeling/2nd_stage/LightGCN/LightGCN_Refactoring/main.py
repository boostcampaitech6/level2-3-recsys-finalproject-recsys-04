import torch
from torch.optim import Adam
import argparse
from preprocessing import Preprocess
from modeling import LightGCN
from train import train, evaluate
from recommend import load_model, encode_session_items,infer_embeddings,recommend_item,recommend_users,random_item
import pandas as pd



def main(args):
    device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')
    config = {
        "emb_dim": 64,
        "n_layers": 3,
        "reg": 0.00001,
        "node_dropout": 0.1,
        "lr": 0.001,
        "num_epochs": 50,
        "n_batch": 256,  
        "model_path": "/home/siyun/ephemeral/LightGCN_Recommender/models",  # 모델의 경로
        "model_name": "lightgcn_model_filtered.pt", # 모델 이름
        'device' : 'device',
        'weight_decay' : 0.0001,
        "data" : '/home/siyun/ephemeral/LightGCN_Recommender/data/filtered_data.csv',   # 파일 경로
        'data_path' : '/home/siyun/ephemeral/LightGCN_Recommender/data/'
    }
    preprocess = Preprocess(config['data'], config)
    model = LightGCN(preprocess.num_users, preprocess.num_items, config['emb_dim'], config['n_layers'], config['reg'], preprocess.adjacency_matrix, device)

    if args.train:
        optimizer = Adam(model.parameters(), lr=config['lr'], weight_decay=config['weight_decay'])
        for epoch in range(config["num_epochs"]):
            train_loss = train(model, preprocess, optimizer, config['n_batch'], device)
            print(f"Epoch {epoch}, Training Loss: {train_loss}")
            recall, precision, f1 = evaluate(model, preprocess.user_item_matrix, preprocess.user_item_matrix, 10, device)
            print(f"Epoch {epoch}, Recall: {recall}, Precision: {precision}, F1: {f1}")
            # Save model if it's the best so far, based on F1 score for simplicity
            if epoch == 0 or f1 > best_f1:
                best_f1 = f1
                torch.save(model.state_dict(), config['model_path'])
                print("Saved new best model")
    else:
        model_path = config["model_path"] + '/' + config["model_name"]
        model = load_model(model_path, model, device)
        session_items = ['B00IQZZEYS','B00KW4LIJQ','B00KREP1HQ','B00LMU8IRE','B00PITUJZE']  # 여기에 새로운 유저의 아이템 히스토리 입력
        top_k = 10
        encoded_session_items = encode_session_items(preprocess, session_items)
        session_user_embedding, item_embeddings, user_embeddings = infer_embeddings(model, encoded_session_items, preprocess.num_users, preprocess.num_items, device)
        
        if args.rec == 'item' : 
            # 아이템 추천이면 여기
            recommended_user_indices = recommend_item(session_user_embedding, item_embeddings, top_k)
            recommended_items = [preprocess.item_decoder[idx] for idx in recommended_user_indices if idx in preprocess.item_decoder]
            print("Recommended Items:", recommended_items)
        
        elif args.rec == 'user' :
            data = pd.read_csv(config['data_path'] + 'filtered_data.csv')
            unique_user_ids = data['user_id'].unique()
            id2idx = {user_id: idx for idx, user_id in enumerate(unique_user_ids)}
            idx2id = {idx: user_id for user_id, idx in id2idx.items()}    
            # 유사한 유저의 아이템 추천이면 여기
            top_k_users = 15  # 행동 패턴이 유사한 상위 K명의 사용자
            # id2idx가 반환됨
            recommended_user_indices = recommend_users(session_user_embedding, user_embeddings, top_k_users)
            # idx2id
            recommended_user_ids = [idx2id[idx] for idx in recommended_user_indices]

            random_item(recommended_user_ids,data,top_k_users)

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('--train', action='store_true', help='Train the model with the given data')
    parser.add_argument('--rec', choices=['item', 'user'], default='item', help='아이템 추천 or 유저추천 선택')
    args = parser.parse_args()
    main(args)
