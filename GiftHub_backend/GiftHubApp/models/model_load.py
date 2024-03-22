import os
import mlflow
import torch
from django.conf import settings

# naver
model_ca_proba = mlflow.pyfunc.load_model(settings.LGBM_PATH)

# amazon
model_bert4rec = torch.load(os.path.join(settings.BERT4REC_PATH, "data/model.pth"), map_location=torch.device(settings.DEVICE))
model_ease = torch.load(os.path.join(settings.EASE_PATH, "data/model.pth"), map_location=torch.device(settings.DEVICE))
model_lightgcn = torch.load(os.path.join(settings.LGCN_PATH, "data/model.pth"), map_location=torch.device(settings.DEVICE))