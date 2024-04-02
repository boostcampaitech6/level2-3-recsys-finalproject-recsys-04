import pandas as pd
from django.conf import settings

from GiftHubApp.database.sql_executor import *
from GiftHubApp.database.serializers import *
from GiftHubApp.database.models import *
from GiftHubApp.api.requests.request import APIRequest

# mlflow naver serving
def predict_lgbm(product_id: str):
    queryset = FilteredRawdata.objects
    serializer = FilteredRawdataSerializer(queryset, many=True)
    df = pd.DataFrame.from_dict(serializer.data)
    df = df.drop("id", axis=1) # id 제외
    
    api = APIRequest()
    columns = list(df.columns)
    data = list(df.loc[:].values.tolist())
    params = {
        "columns":columns,
        "rows":data,
        "product_id":product_id
    }
    api.set_data(params)
    api.set_url(settings.MODEL_SERVING_URL + settings.LGBM_SLASH)
    predictions = api.post()
    predictions = pd.DataFrame(predictions["rows"], columns=predictions["columns"])
    
    return predictions

# amazon product serving
def predict_bert4rec(list_product_id: list):
    api = APIRequest()
    params = {
        "matrix":list_product_id
    }
    api.set_data(params)
    api.set_url(settings.MODEL_SERVING_URL + settings.BERT4REC_SLASH)
    predictions = api.post()
    predictions = predictions["list"]
    
    return predictions

def predict_ease(df_user_interaction: pd.DataFrame):
    api = APIRequest()
    columns = list(df_user_interaction.columns)
    data = list(df_user_interaction.loc[:].values.tolist())
    params = {
        "columns":columns,
        "rows":data
    }
    api.set_data(params)
    api.set_url(settings.MODEL_SERVING_URL + settings.EASE_SLASH)
    predictions = api.post()
    predictions = predictions["list"]
    
    return predictions

def predict_lightgcn(list_product_id: list):
    api = APIRequest()
    params = {
        "matrix":list_product_id
    }
    api.set_data(params)
    api.set_url(settings.MODEL_SERVING_URL + settings.LGCN_SLASH)
    predictions = api.post()
    predictions = predictions["list"]
    
    return predictions