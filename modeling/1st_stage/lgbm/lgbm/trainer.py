import os
import wandb
import numpy as np

import pickle
import mlflow

from .model import *
from .logger import get_logger, logging_conf, get_save_time


logger = get_logger(logger_conf=logging_conf)


def train_validate(argument, all_data, model):
    # 학습 + valid 예측
    model = model.fit(all_data)
    
    # 모델 저장
    os.makedirs(name=argument.model_dir, exist_ok=True)
    pickle.dump(model, open(f'{argument.model_dir}{argument.model}.pkl', 'wb'))
    mlflow.sklearn.log_model(model, "category_predict")

# def inference(argument, test_data, model):
#     # 학습된 모델로 추론
#     predict = model.predict(test_data[argument.features_col])
    
#     # 시간저장 + test파일 저장
#     save_time = get_save_time()
#     write_path = os.path.join(argument.output_dir, f"submission_{save_time}_{argument.model}" + ".csv")
#     os.makedirs(name=argument.output_dir, exist_ok=True)
#     with open(write_path, "w", encoding="utf8") as w:
#         w.write("id,prediction\n")
#         for id, p in enumerate(predict):
#             w.write("{},{}\n".format(id, p))

#     logger.info("Successfully saved submission as %s", write_path)

def get_model(argument, all_data):
    model_name = argument.model.lower()
    if model_name == 'lgbm':
        model = lgbm(argument, all_data)
    return model