import sys, os
import mlflow
import torch
from django.conf import settings

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(os.path.dirname(__file__)))))
from mlartifacts.bert4rec.model import BERT4Rec, params

# naver
model_ca_proba = mlflow.pyfunc.load_model(settings.PATH_CATEGORY_PROBA)

# amazon
model_bert4rec = BERT4Rec(**params)
model_bert4rec.load_state_dict(torch.load(os.path.join(settings.PATH_BERT4REC, "model.pt")))
model_bert4rec.to(params["device"])