import torch
from pydantic import Field
from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    MODEL_DOWNLOAD_YN: str = Field(default="N", env="MODEL_DOWNLOAD_YN")
    DEVICE: str = "cuda" if torch.cuda.is_available() else "cpu"
    MLFLOW_URL: str = Field(default="http://175.45.193.211:8010", env="MLFLOW_URL")
    
    LGBM_PATH: str = Field(default="models/category_proba", env="LGBM_PATH")
    BERT4REC_PATH: str = Field(default="models/BERT4Rec", env="BERT4REC_PATH")
    EASE_PATH: str = Field(default='models/EASE', env="EASE_PATH")
    LGCN_PATH: str = Field(default="models/lightgcn", env="LGCN_PATH")
    LGBM_VER: str = Field(default="models:/ca_proba/1", env="LGBM_VER")
    BERT4REC_VER: str = Field(default="models:/bert4rec/4", env="BERT4REC_VER")
    EASE_VER: str = Field(default="models:/ease/1", env="EASE_VER")
    LGCN_VER: str = Field(default="models:/lightgcn/1", env="LGCN_VER")
    
    class Config:
        env_file = "setting.env"
        env_file_encoding = 'utf-8'

settings = Settings()