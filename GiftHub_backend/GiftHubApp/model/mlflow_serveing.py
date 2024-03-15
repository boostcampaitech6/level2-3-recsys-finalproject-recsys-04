import pandas as pd
import numpy as np

from GiftHubApp.database.sql_executor import *
from GiftHubApp.database.serializers import *
from GiftHubApp.database.models import *
from GiftHubApp.api.requests.request import *
from GiftHubApp.model.mlflow_load_model import model_ca_proba

def lgbm_similarlity(product_id):
    queryset = FilteredRawdata.objects
    serializer = Temp02Serializer(queryset, many=True)
    df = pd.DataFrame.from_dict(serializer.data)
    df = df.drop("id", axis=1) # id 제외
    df.loc[df["category_3"]=="", "category_3"] = np.nan
    
    filtered_encoding = pd.get_dummies(df, columns=['category_1','category_2','category_3'])
    data_index = filtered_encoding.copy()
    unique_product_ids = np.unique(data_index['product_id']).tolist()
    # id2idx: 각 product_id를 연속적인 정수 인덱스로 매핑
    id2idx = {product_id: idx for idx, product_id in enumerate(unique_product_ids)}

    # idx2id: 연속적인 정수 인덱스를 원래의 product_id로 매핑
    idx2id = {idx: product_id for product_id, idx in id2idx.items()}
    data_index['mapped_product_id'] = data_index['product_id'].apply(lambda x: id2idx[x])
    cols = list(data_index.columns)
    
    features = cols.copy()

    # 새로운 feature 리스트 생성
    removes = ['product_id','mapped_product_id', 'product_name', 'brand', 'image_url', 'product_url']
    for remove in removes : 
        features.remove(remove)
    target = ['mapped_product_id']
    
    X = data_index[features]
    y = data_index[target]
    
    prob = model_ca_proba.predict(X)
    
    # 가장 확률이 높은 클래스의 인덱스 찾기
    highest_prob_index = np.argmax(prob, axis=1)
    # 가장 확률이 높은 클래스에 대한 확률 선택
    
    # 가장 확률이 높은 클래스의 인덱스를 사용하여 실제 product_id를 매핑 (가정: model.classes_에 매핑 정보가 있음)
    predicted_product_ids = [idx2id[idx] for idx in highest_prob_index]
    
    highest_prob = np.max(prob, axis=1)
    
    # 결과를 데이터에 추가
    data_index['predicted_product_id'] = predicted_product_ids
    data_index['highest_probability'] = highest_prob
    
    top_similar_products = find_similar_products(product_id, data_index, n=27)
    
    return top_similar_products
    
def find_similar_products(user_product_id, product_id_prob, n=10):
    """
    주어진 product_id에 대해 상위 n개의 가장 유사한 predicted_product_id를 찾습니다.
    
    Args:
    - user_product_id: 유저의 product_id.
    - product_id_prob: 예측된 product_id와 그 확률이 포함된 DataFrame.
    - n: 반환할 유사한 product_id의 개수.
    
    Returns:
    - 상위 n개의 가장 유사한 predicted_product_id 리스트.
    """

    if user_product_id not in product_id_prob['product_id'].values:
        print("Product ID not found in the DataFrame.")
        return []
    
    # 해당 product_id에 대한 predicted_product_id 찾기
    predicted_product_id = product_id_prob[product_id_prob['product_id'] == user_product_id]['predicted_product_id'].values[0]
    
    
    # 유사도 계산이나 로직에 따라 상위 n개의 유사한 product_id 선택
    # 여기서는 예시로, 해당 product_id의 행을 제외하고 랜덤으로 n개를 선택합니다.
    # 실제 구현에서는 유사도 계산을 통해 이를 결정해야 합니다.
    similar_products = product_id_prob[product_id_prob['product_id'] != user_product_id][['predicted_product_id', 'image_url']].sample(n=n)
    similar_products = similar_products.rename(columns={'predicted_product_id': 'product_id'})
    
    return similar_products