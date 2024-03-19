import sys, os
import mlflow
import torch
from django.conf import settings

# naver
model_ca_proba = mlflow.pyfunc.load_model(settings.PATH_CATEGORY_PROBA)

# amazon
model_bert4rec = torch.load(os.path.join(settings.PATH_BERT4REC, "model.pt"))
model_ease = torch.load(os.path.join(settings.PATH_EASE, "20240318_013556_EASE.pt"))