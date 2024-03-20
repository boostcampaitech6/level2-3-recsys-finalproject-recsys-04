import os
import torch
from torch.optim import Adam
import argparse
from preprocessing import Preprocess
from modeling import LightGCN
from train import train, evaluate
from recommend import load_model, encode_session_items,infer_embeddings,recommend_item




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
        "model_path": "/home/ksh/GiftHub_model/modeling/amazon_cf/lightgcn/",  # 모델의 경로
        "model_name": "lightgcn_model_filtered.pt", # 모델 이름
        'device' : 'device',
        'weight_decay' : 0.0001,
        "data_path" : '/home/ksh/GiftHub_model/modeling/amazon_cf/data/filtered_data.csv'   # 파일 경로
    }
    preprocess = Preprocess(config['data_path'], config)
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
                torch.save(model, os.path.join(config["model_path"], config["model_name"]))
                print("Saved new best model")
    else:
        model_path = config["model_path"] + '/' + config["model_name"]
        model = torch.load(os.path.join(model_path))
        session_items = ['B00IQZZEYS','B00KW4LIJQ','B00KREP1HQ','B00LMU8IRE','B00PITUJZE']  # 여기에 새로운 유저의 아이템 히스토리 입력
        top_k = 10
        encoded_session_items = encode_session_items(preprocess, session_items)
        session_user_embedding, item_embeddings = infer_embeddings(model, encoded_session_items, preprocess.num_users, preprocess.num_items, device)
        recommended_user_indices = recommend_item(session_user_embedding, item_embeddings, top_k)
        recommended_items = [preprocess.item_decoder[idx] for idx in recommended_user_indices if idx in preprocess.item_decoder]
        print("Recommended Items:", recommended_items)

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('--train', action='store_true', help='Train the model with the given data')
    args = parser.parse_args()
    main(args)