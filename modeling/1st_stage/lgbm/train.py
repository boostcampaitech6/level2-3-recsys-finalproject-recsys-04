import os

import numpy as np
import torch
import wandb

from lgbm import trainer
from lgbm.argument import parse_args
from lgbm.dataloader import Preprocess
from lgbm.logger import get_logger, set_seeds, logging_conf

import mlflow


logger = get_logger(logging_conf)


def main(argument):
    #wandb.login()
    set_seeds(argument.seed)
    
    # data load + data 처리 
    logger.info("Preparing data ...")
    preprocess = Preprocess(argument)
    df = preprocess.load_data_from_file() # db에서 데이터를 받아와서 전처리 후 df로 반환
    preprocess.load_all_data(df) # 데이터 로드한 것을 none이었던 self.all_data에 정의
    all_data = preprocess.get_all_data() # self.all_data을 반환

    mlflow.set_tracking_uri(uri="http://101.79.11.75:8010")
    mlflow.set_experiment("category_predict")
    mlflow.lightgbm.autolog()

    # 모델 선택
    with mlflow.start_run() as run:
        logger.info("Building Model ...")
        model = trainer.get_model(argument=argument, all_data=all_data)
    
        # 학습 실행
        logger.info("Start Training ...")
        trainer.train_validate(argument, all_data, model)
    

if __name__ == "__main__":
    argument = parse_args() # 인자들 저장
    
    os.makedirs(argument.model_dir, exist_ok=True)
    main(argument) # main함수 실행 -> 학습!!!!!!!!!!!