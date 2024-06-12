import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
import warnings
warnings.filterwarnings('ignore')

# data loading
path = '/home/siyun/ephemeral/data/'
df = pd.read_csv(path + 'gift_data.csv')

df['category_3'].fillna('unknown', inplace=True)
product_category_counts = df.groupby(['product_id', 'category_1', 'category_2', 'category_3']).size().reset_index(name='counts')

# 각 product_id 내에서 카테고리가 선택될 확률 계산
product_category_counts['total_counts'] = product_category_counts.groupby('product_id')['counts'].transform('sum')
product_category_counts['prob'] = product_category_counts['counts'] / product_category_counts['total_counts']

# 각 product_id에 대한 엔트로피를 계산
# -sigma(pi) * log2(pi)
product_category_counts['personality'] = -product_category_counts['prob'] * np.log2(product_category_counts['prob'])
product_entropy = product_category_counts.groupby('product_id')['personality'].sum().reset_index()

# 매핑
mean_entropy = product_entropy['personality'].mean()
df = df.merge(product_entropy, on='product_id', how='left')
df['personality'].fillna(mean_entropy, inplace=True)


# outlier filtering
filtered_df = pd.DataFrame()
for col1 in df['category_1'].unique():
    # 특정 category_1 값에 해당하는 행들만 선택
    filtered_df1 = df[df['category_1'] == col1]

    # category_2의 unique 값에 대해 반복
    for col2 in filtered_df1['category_2'].unique():
        # 특정 category_2 값에 해당하는 행들만 선택
        filtered_df2 = filtered_df1[filtered_df1['category_2'] == col2]

        # 각 카테고리1의 하위 카테고리인 카테고리2의 quantile 0.3 이하를 제거 
        price_q_3 = filtered_df2['price'].quantile(0.3)
        price_q_99 =  filtered_df2['price'].quantile(0.99)
        rev_q_0_50 = filtered_df2['num_review'].quantile(0.5)

        filtered_q3 = filtered_df2[(filtered_df2['price'] > price_q_3) & (filtered_df2['price'] <= price_q_99) & (filtered_df2['num_review'] >= rev_q_0_50)]
        filtered_df = pd.concat([filtered_df, filtered_q3])


# 카테고리1 별 비율 계산
cat1_ratios = filtered_df['category_1'].value_counts(normalize=True)

# 샘플링할 최종 데이터프레임 초기화
final_sample_df = pd.DataFrame()

# 총 샘플링할 개수
total_samples = 30000

# 카테고리1 별로 루프
for cat1, cat1_ratio in cat1_ratios.items():
    cat1_df = filtered_df[filtered_df['category_1'] == cat1]

    # 카테고리1의 비율에 따라 할당할 샘플 수 계산 (1 - 카테고리1의 비율)
    cat1_sample_size = int((cat1_ratio) * total_samples)
    # 카테고리2 별 비율 계산
    cat2_ratios = cat1_df['category_2'].value_counts(normalize=True)
    # 카테고리2 별로 샘플링
    for cat2, cat2_ratio in cat2_ratios.items():
        cat2_df = cat1_df[cat1_df['category_2'] == cat2]
        # 카테고리2 별 할당할 샘플 수 (카테고리2의 비율 * 카테고리1 내 샘플 수)
        cat2_sample_size = max(3, int(cat2_ratio * cat1_sample_size)) # 적어도 3개는 샘플링
        # 샘플링 후 최종 데이터프레임에 추가
        sampled_df = cat2_df.sample(n=cat2_sample_size, replace=False) # replace=False로 중복 없이 추출
        final_sample_df = pd.concat([final_sample_df, sampled_df])

# 최종 샘플링된 데이터프레임의 길이 조정
## total_samples보다 많이 샘플링된 경우 조정 필요 
if len(final_sample_df) > total_samples:
    final_sample_df = final_sample_df.sample(n=total_samples)


product_id_counts = final_sample_df['product_id'].value_counts()
# 빈도가 2 이상인 product_id 선택
valid_product_ids = product_id_counts[product_id_counts >= 3].index
# 해당 product_id만 포함하는 행을 필터링
final_sample_df_freq_2= final_sample_df[final_sample_df['product_id'].isin(valid_product_ids)]

# final_sample_df_freq_2.to_csv('/home/siyun/ephemeral/data/filtered_gift.csv', index=False)

filtered_encoding = pd.get_dummies(final_sample_df_freq_2, columns=['category_1','category_2','category_3'])
data_index = filtered_encoding.copy()
unique_product_ids = np.unique(data_index['product_id']).tolist()

# id2idx: 각 product_id를 연속적인 정수 인덱스로 매핑
# idx2id: 연속적인 정수 인덱스를 원래의 product_id로 매핑
id2idx = {product_id: idx for idx, product_id in enumerate(unique_product_ids)}
idx2id = {idx: product_id for product_id, idx in id2idx.items()}
data_index['mapped_product_id'] = data_index['product_id'].apply(lambda x: id2idx[x])
cols = list(data_index.columns)

features = cols.copy()
# 새로운 feature 리스트 생성
removes = ['product_id','mapped_product_id', 'product_name', 'brand', 'image_url', 'product_url']
for remove in removes : 
    features.remove(remove)
target = ['mapped_product_id']

# 모델링
from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import train_test_split
from sklearn.metrics import f1_score
from sklearn.model_selection import StratifiedKFold
from sklearn.model_selection import train_test_split
from sklearn.metrics import f1_score, accuracy_score, recall_score, precision_score, roc_auc_score, confusion_matrix
from lightgbm import LGBMClassifier
import wandb
import pickle
from sklearn.metrics.pairwise import cosine_similarity

X = data_index[features]
y = data_index[target]

# train, test, valid로 나눕시다
train_x,test_x,train_y,test_y = train_test_split(X,y, test_size=0.25, random_state=42, stratify=y)

params = {
    'learning_rate': 0.01794243998188023,  
    'num_leaves': 4,      
    'n_estimators': 20,    
    'max_depth': 4,         
    'device_type' : 'cuda' 
}

# 전체 데이터에 대한 모델 학습 함수
def train_full_model(X, y, params):
    num_classes = y.nunique()
    model = LGBMClassifier(
        objective='multiclass',
        num_class=num_classes,
        learning_rate=params['learning_rate'],
        num_leaves=params['num_leaves'],
        n_estimators=params['n_estimators'],
        max_depth=params['max_depth'],
        verbose=-1,
        device_type=params['device_type']
    )
    model.fit(X, y)
    return model

# 모델 저장
# model_save_path = "/home/siyun/ephemeral/boosting/output/n30000_7469_lgbm_lr_01794243998188023_lea_4_esti_20_dep_4.pkl"  # 변경된 경로
# with open(model_save_path, "wb") as file:
#     pickle.dump(model, file)
# with open(model_save_path, 'rb') as file:
#     loaded_model = pickle.load(file)

def add_prediction_probabilities(models, X, data, target):
    # 해당 모델에 대한 확률 계산
    prob = model.predict_proba(X)
    # 가장 확률이 높은 클래스의 인덱스 찾기
    highest_prob_index = np.argmax(prob, axis=1)
    # 가장 확률이 높은 클래스에 대한 확률 선택
    # 가장 확률이 높은 클래스의 인덱스를 사용하여 실제 product_id를 매핑
    predicted_product_ids = [idx2id[idx] for idx in highest_prob_index]
    highest_prob = np.max(prob, axis=1)
    # 결과를 데이터에 추가
    data['predicted_product_id'] = predicted_product_ids
    data['highest_probability'] = highest_prob
    return data

# train_x에 대한 inference
## pkl로 받은 모델을 사용하기 위해서는 model -> loaded_model
final_prediction = add_prediction_probabilities(model, X, data_index.copy(), 'mapped_product_id')

def find_similar_products(inference, user_product_id, n=10):
    """
    주어진 product_id에 대해 상위 n개의 가장 유사한 predicted_product_id를 찾습니다.
    Args:
    - infernce: 예측된 product_id와 그 확률이 포함된 DataFrame.
    - user_product_id: 유저의 product_id.
    - n: 반환할 유사한 product_id의 개수.
    
    Method:
    - 카테고리를 바탕으로 유사도를 계산
    - 예측된 product_id가 해당하는 카테고리의 다른 아이템들간의 유사도를 계산하여 높은 것을 반환. 
    - 추가적으로 다른 scaled data도 고려하여 유사도를 계산

    Returns:
    - 상위 n개의 가장 유사한 predicted_product_id 리스트.
    """
    unique_products = inference.sort_values(by='highest_probability', ascending=False).drop_duplicates(subset='product_id', keep='first').reset_index(drop=True)

    category_columns = [col for col in unique_products.columns if 'category' in col]
    features = unique_products[category_columns]
    
    # user_product_id가 unique_products에 존재하는지 확인
    if user_product_id in unique_products['product_id'].values:
        # target_idx를 인덱스 값이 아닌 위치로 사용
        target_idx = unique_products.index[unique_products['product_id'] == user_product_id].tolist()[0]
        target_features = features.loc[[target_idx]]
        target_features_2d = target_features.values.reshape(1, -1)
        sim = cosine_similarity(target_features_2d, features)[0]

        sim[target_idx] = -1  # 자기 자신 제외
        similar_indices = sim.argsort()[::-1][:n]
        similar_product_ids = unique_products.iloc[similar_indices]['product_id'].tolist()
        return similar_product_ids
    else:
        # user_product_id에 해당하는 데이터가 없는 경우
        return []

# user_product_id를 입력받으면 유사도 계산 -> topk 개의 유사한 아이템 반환
user_product_id=2864497971
top_similar_products = find_similar_products(final_prediction, user_product_id, n=10)






