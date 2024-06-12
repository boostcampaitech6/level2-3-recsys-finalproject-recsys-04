import os

import numpy as np
import torch
import wandb
import pickle

from lgbm import trainer
from lgbm.argument import parse_args
from lgbm.dataloader import Preprocess
from lgbm.logger import get_logger, set_seeds, logging_conf


logger = get_logger(logging_conf)


def main(argument):
    wandb.login()
    set_seeds(argument.seed)
    
    # data load + data 처리 
    logger.info("Preparing data ...")
    preprocess = Preprocess(argument)
    df = preprocess.load_data_from_file() # db에서 데이터를 받아와서 전처리 후 ndarray로 반환
    preprocess.load_test_data(df) # 데이터 로드한 것을 none이었던 self.test_data에 정의
    test_data = preprocess.get_test_data() # self.test_data을 반환
    
    # 모델 선택
    logger.info("Building Model ...")
    model = pickle.load(open(f'{argument.model_dir}{argument.model}.pkl', 'rb'))
    
    # 학습 실행
    logger.info("Inference")
    trainer.inference(argument, test_data, model)
    
    

if __name__ == "__main__":
    argument = parse_args() # 인자들 저장
    
    os.makedirs(argument.model_dir, exist_ok=True)
    main(argument) # main함수 실행 -> 학습!!!!!!!!!!!