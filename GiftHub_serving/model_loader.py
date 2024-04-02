import sys, os
import mlflow
import torch
from config import settings

sys.path.append(os.path.join(os.path.join(os.path.dirname(__file__), "models"), "BERT4Rec"))
sys.path.append(os.path.join(os.path.join(os.path.dirname(__file__), "models"), "EASE"))
sys.path.append(os.path.join(os.path.join(os.path.dirname(__file__), "models"), "lightgcn"))

class Model():
    def load(self):
        # naver
        self.ca_proba = mlflow.pyfunc.load_model(settings.LGBM_PATH)
        # amazon
        self.bert4rec = torch.load(os.path.join(settings.BERT4REC_PATH, "data/model.pth"), map_location=torch.device(settings.DEVICE))
        self.ease = torch.load(os.path.join(settings.EASE_PATH, "data/model.pth"))
        self.lightgcn = torch.load(os.path.join(settings.LGCN_PATH, "data/model.pth"), map_location=torch.device(settings.DEVICE))
        
    def download(self):
        from main import settings
        # mlflow model download
        mlflow.artifacts.download_artifacts(artifact_uri=settings.LGBM_VER, dst_path=settings.LGBM_PATH)
        mlflow.artifacts.download_artifacts(artifact_uri=settings.BERT4REC_VER, dst_path=settings.BERT4REC_PATH)
        mlflow.artifacts.download_artifacts(artifact_uri=settings.EASE_VER, dst_path=settings.EASE_PATH)
        mlflow.artifacts.download_artifacts(artifact_uri=settings.LGCN_VER, dst_path=settings.LGCN_PATH)
        
model = Model()