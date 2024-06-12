import sys
import time
import logging
import argparse

import torch
import pandas as pd
from src.EASE import TorchEASE
from src.utils import set_seed, check_path, recall_at_k

logger = logging.getLogger("notebook")

def main(args):
    
    # seed, time settings
    set_seed(args.seed)
    check_path(args.output_dir)

    now = time.localtime()
    now_date = time.strftime('%Y%m%d', now)
    now_hour = time.strftime('%X', now)
    save_time = now_date + '_' + now_hour.replace(':', '')

    # file path setttings
    input_dir = "./data/"
    output_dir = "./output/"
    train_csv_file = "trainset_amazon_fashion.csv"
    test_csv_file = "testset_amazon_fashion.csv"
    output_file = f'{save_time}_EASE.pt'

    # model column name settings 
    user_col = "reviewerID"
    item_col = "asin"
    score_col = None #implicit feedback

    if args.train:
        ######################## DATA LOAD
        train_df = pd.read_csv(input_dir+train_csv_file)
        test_df = pd.read_csv(input_dir+test_csv_file)

        ######################## TRAIN
        logger.info("Training model")
        model = TorchEASE(train_df, user_col=user_col, item_col=item_col, score_col=score_col, reg=args.reg)
        model.fit()

        logger.info("Model test")
        predict_top_k = model.predict_all(test_df, k=10)
        predicted_items = predict_top_k.set_index('reviewerID').to_dict()['predicted_items']
        # 중복되는 reviewerID를 가진 행을 그룹화하고 asin 값을 리스트로 수집하여 딕셔너리에 저장
        grouped = test_df.groupby('reviewerID')['asin'].apply(list).reset_index(name='true_item')
        # 원래 데이터프레임과 병합하여 새로운 true_item 컬럼을 추가
        test_df = pd.merge(test_df, grouped, on='reviewerID', how='left')
        # 데이터프레임을 딕셔너리로 변환
        actual_items = test_df.set_index('reviewerID').to_dict()['true_item']

        # 성능 확인
        recall = recall_at_k(actual_items, predicted_items, k=10)
        print("Recall@10:", recall)

        # 모델 저장
        torch.save(model,output_dir+output_file)
        logger.info("model saved.")

    else:
        # 모델 불러오기
        model = torch.load(output_dir+"20240318_013556_EASE.pt")

        # userid : 'reviewerID, itemid :'asin'
        new_data = pd.read_csv('./data/client_test_data.csv')

        # 새로운 데이터에 맞게 finetuning
        model.fine_tune(new_data)
        
        # 클라이언트 input에 대한 predict
        client_result = model.predict_all(new_data, k=10)

        print("predict top 10 : ", client_result['predicted_items'][0])

if __name__ == "__main__":


    parser = argparse.ArgumentParser()

    parser.add_argument("--output_dir", default="output/", type=str)
    parser.add_argument("--data_name", default="trainset_amazon_fashion", type=str)

    # model args
    parser.add_argument("--reg", default=0.05, type=int)
    
    # train args
    parser.add_argument("--seed", default=42, type=int)
    parser.add_argument("--gpu_id", type=str, default="0", help="gpu_id")
    parser.add_argument("--train", action="store_true")

    args = parser.parse_args()
    main(args)