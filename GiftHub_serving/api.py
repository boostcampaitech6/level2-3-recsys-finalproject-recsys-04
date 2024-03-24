import pandas as pd
from model_serving import *

from fastapi import APIRouter, HTTPException
from starlette.responses import JSONResponse
from config import settings
from utils import df_to_dict, list_to_dict

from base import DataTable, Matrix, LGBMData

router = APIRouter()

# "/"로 접근하면 return을 보여줌
@router.get("/")
def read_root():
    return {settings.BERT4REC_PATH}

# "/"로 접근하면 return을 보여줌
@router.post("/naver/model/lgbm")
def read_root(filtered_data: LGBMData):
    df = pd.DataFrame(filtered_data.rows, columns=filtered_data.columns)
    product_id = filtered_data.product_id
    
    predictions = predict_lgbm(product_id, df)
    predictions = df_to_dict(predictions)
    
    return predictions

# "/"로 접근하면 return을 보여줌
@router.post("/amazon/model/bert4rec")
def read_root(list_product_id: Matrix):
    predictions = predict_bert4rec(list_product_id.matrix)
    predictions = list_to_dict(predictions)
    
    return predictions

@router.post("/amazon/model/ease")
def read_root(user_interaction: DataTable):
    df = pd.DataFrame(user_interaction.rows, columns=user_interaction.columns)
    
    predictions = predict_ease(df)
    predictions = list_to_dict(predictions)
    
    return predictions

@router.post("/amazon/model/lightgcn")
def read_root(list_product_id: Matrix):
    predictions = predict_lightgcn(list_product_id.matrix)
    predictions = list_to_dict(predictions)
    
    return predictions