import pandas as pd
import numpy as np
import torch
import torch.nn as nn
from torch.utils.data import Dataset, DataLoader
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder

import os
os.environ['CUDA_LAUNCH_BLOCKING'] = "1"

device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')
print(f"using {device} ")

df = pd.read_csv('/home/siyun/ephemeral/WDN/data/gift_data.csv')

# 개성
## 각 product_id 별로 size(count) 계산
## 개성 == 각 카테고리별로 entropy계산한 것이라 논리에 맞지 않을 수도 있음.
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

###########
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
total_samples = 115086

# 카테고리1 별로 루프
for cat1, cat1_ratio in cat1_ratios.items():
    cat1_df = filtered_df[filtered_df['category_1'] == cat1]
    # print(cat1_ratio)
    
    # 카테고리1의 비율에 따라 할당할 샘플 수 계산 (1 - 카테고리1의 비율)
    cat1_sample_size = int((cat1_ratio) * total_samples)
    # print(cat1_sample_size)
    
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
## total_samples보다 많이 샘플링된 경우 조정
if len(final_sample_df) > total_samples:
    final_sample_df = final_sample_df.sample(n=total_samples)



product_id_counts = final_sample_df['product_id'].value_counts()
## 빈도가 3 이상인 product_id 선택
valid_product_ids = product_id_counts[product_id_counts >= 3].index
## 해당 product_id만 포함하는 행을 필터링
final_sample_df_freq_2= final_sample_df[final_sample_df['product_id'].isin(valid_product_ids)]

# 받아서 사용하려면 저장
## final_sample_df_freq_2.to_csv('/home/siyun/ephemeral/data/filtered_gift.csv', index=False)

filtered_data = final_sample_df_freq_2
filtered_data = filtered_data.drop(['image_url','product_url'], axis=1)

id2idx = {id: idx for idx, id in enumerate(sorted(filtered_data['product_id'].unique()))}
idx2id = {idx: id for id, idx in id2idx.items()}
filtered_data['product_idx'] = filtered_data['product_id'].map(id2idx)


from sklearn.preprocessing import StandardScaler
from torch.utils.data import TensorDataset, DataLoader, Dataset
categorical_columns = ['brand','category_1', 'category_2', 'category_3']
continuous_columns = ['rating', 'num_review', 'price', 'personality']

def dl_data_split(data, test_size=0.2, seed=42):
    X = data[categorical_columns + continuous_columns]
    y = data['product_idx']
    
    X_train, X_valid, y_train, y_valid = train_test_split(
    X, y, test_size=test_size, random_state=seed, stratify=y
)
    
    ## 연속형 데이터 스케일링
    scaler = StandardScaler()
    X_train[continuous_columns] = scaler.fit_transform(X_train[continuous_columns])
    X_valid[continuous_columns] = scaler.transform(X_valid[continuous_columns])
    
    return X_train, X_valid, y_train, y_valid


X_train, X_valid, y_train, y_valid = dl_data_split(filtered_data)

# Dataset & DataLoader
## 기본제공되는 TensorDataset은 categorical과 continuous를 나누어서 받지 못함. 따라서 customdataset이 필요
class Cat_Con_Dataset(Dataset):
    def __init__(self, X, y):
        self.X_cat = torch.tensor(X[categorical_columns].values, dtype=torch.long)
        self.X_cont = torch.tensor(X[continuous_columns].values, dtype=torch.float)
        self.y = torch.tensor(y.values, dtype=torch.long)
        print("Label sample in dataset initialization:", self.y[:10])

    def __len__(self):
        return len(self.y)

    def __getitem__(self, idx):
        return self.X_cat[idx], self.X_cont[idx], self.y[idx]

## 데이터 로더 생성
def dl_data_loader(X_train, y_train, X_valid, y_valid, batch_size=64, shuffle=True):
    train_dataset = Cat_Con_Dataset(X_train, y_train)
    valid_dataset = Cat_Con_Dataset(X_valid, y_valid)
    
    train_dataloader = DataLoader(train_dataset, batch_size=batch_size, shuffle=shuffle)
    valid_dataloader = DataLoader(valid_dataset, batch_size=batch_size, shuffle=False)
    
    return train_dataloader, valid_dataloader

train_dataloader, valid_dataloader = dl_data_loader(X_train, y_train, X_valid, y_valid)

# Model 구조
class WideAndDeepModel(nn.Module):
    def __init__(self, categorical_field_dims, continuous_field_dims, embed_dim, mlp_dims, dropout):
        super().__init__()
        self.categorical_embedding = nn.ModuleList([nn.Embedding(num_embeddings=dim, embedding_dim=embed_dim) for dim in categorical_field_dims])
        self.continuous_linear = nn.Linear(len(continuous_field_dims), 1)
        total_embed_dim = len(categorical_field_dims) * embed_dim + len(continuous_field_dims)
        self.mlp = nn.Sequential(
            nn.Linear(total_embed_dim, mlp_dims[0]),
            nn.ReLU(),
            nn.Dropout(dropout),
            *[nn.Sequential(nn.Linear(mlp_dims[i], mlp_dims[i+1]), nn.ReLU(), nn.Dropout(dropout)) for i in range(len(mlp_dims)-1)],
            nn.Linear(mlp_dims[-1], 12389)
        )

    def forward(self, x_categorical, x_continuous):
        # print("Input x_categorical:", x_categorical.shape)
        # print("Input x_continuous:", x_continuous.shape)
        x_embedded = [embedding(x_categorical[:, i]) for i, embedding in enumerate(self.categorical_embedding)]
        x_embedded = torch.cat(x_embedded, dim=1)
        # print("After embedding and concatenation:", x_embedded.shape)
        x_total = torch.cat([x_embedded, x_continuous], dim=1)
        # print("After concatenating with continuous:", x_total.shape)
        x_linear = self.continuous_linear(x_continuous)
        # print("Output of continuous linear:", x_linear.shape)
        x_mlp = self.mlp(x_total)
        # print("Output of MLP:", x_mlp.shape)
        output = x_linear + x_mlp
        # print("Final output:", output.shape)
        return output
   
    
# 모델 초기화
categorical_field_dims = [filtered_data['brand'].nunique(), filtered_data['category_1'].nunique(), filtered_data['category_2'].nunique(), filtered_data['category_3'].nunique()]
continuous_field_dims = ['rating', 'personality', 'price_scaling', 'review_scaling']
model = WideAndDeepModel(categorical_field_dims, 
                         continuous_field_dims, 
                         embed_dim=512, mlp_dims=[516, 258, 128,64,32,16], 
                         dropout=0.1).to(torch.device('cuda' if torch.cuda.is_available() else 'cpu'))

optimizer = torch.optim.Adam(model.parameters(), lr=0.0001, weight_decay=1e-7)
criterion = nn.CrossEntropyLoss()

# GPU 사용 설정
device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
model.to(device)


# wandb의 sweep을 사용.
## 바로 사용할거면 구조 변경 필요
import wandb
import torch
from torch import nn
from torch.utils.data import DataLoader
# 모델 및 데이터 로드에 필요한 import 문을 추가하세요

def train():
    # WandB 초기화
    wandb.init(project="wide deep model sweep", config={
        "batch_size": [256,512,1024],
        "lr": [0.001,0.0001],
        "weight_decay": [1e-7,1e-5],
        "embed_dim": [128,256,512,1024],
        "dropout": 0.1,
        "mlp_dims": [512,258, 128, 64, 32, 16],
        "epochs": [100,200,300]
    })

    # Config 가져오기
    config = wandb.config

    # 모델 및 데이터 로드
    # 여기에 모델 및 데이터 로드 코드를 추가하세요

    # 모델 초기화
    model = WideAndDeepModel(categorical_field_dims, 
                             continuous_field_dims, 
                             embed_dim=config.embed_dim, 
                             mlp_dims=config.mlp_dims, 
                             dropout=config.dropout).to(torch.device('cuda' if torch.cuda.is_available() else 'cpu'))

    # 옵티마이저 및 손실 함수 정의
    optimizer = torch.optim.Adam(model.parameters(), lr=config.lr, weight_decay=config.weight_decay)
    criterion = nn.CrossEntropyLoss()

    # 학습 코드 구현
    total_batches = 0  # total_batches 변수 선언 및 초기화
    for epoch in range(config.epochs):
        total_loss = 0
        total_acc = 0
        for batch_idx, batch in enumerate(train_dataloader):
            # 학습 코드 작성
            optimizer.zero_grad()  
            x_categorical, x_continuous, labels = batch
            x_categorical, x_continuous, labels = x_categorical.to(device), x_continuous.to(device), labels.to(device)
            outputs = model(x_categorical, x_continuous)
            loss = criterion(outputs, labels)
            loss.backward()  
            optimizer.step()  
            total_loss += loss.item()

            # 정확도 계산
            _, predicted = torch.max(outputs, 1)
            batch_acc = (predicted == labels).sum().item() / len(labels)
            total_acc += batch_acc
            total_batches += 1

            # WandB에 배치별 정확도 기록
            # wandb.log({f"batch_{batch_idx}_accuracy": batch_acc})
        
        avg_loss = total_loss / len(train_dataloader)
        avg_acc = total_acc / len(train_dataset)

        # wandb에 로그 기록
        wandb.log({"epoch": epoch, "loss": avg_loss, "accuracy": avg_acc})

# WandB sweep 실행
wandb.agent(wandb.sweep({"name": "Wide and Deep Model Sweep_epoches", "method": "grid", "parameters": {
    "batch_size": {"values": [256,512,1024]},
    "lr": {"values": [0.0001, 0.001, 0.01]},
    "weight_decay": {"values": [1e-5,1e-3]},
    "embed_dim": {"values": [128, 256, 512]},
    "dropout": {"values": [0.1, 0.2, 0.3]},
    "mlp_dims": {"values": [[516, 258, 128, 64, 32, 16], [256, 128, 64, 32, 16], [128, 64, 32, 16]]},
    "epochs": {"values": [100,200,300]}
}}), function=train)



# 모든 데이터에서 가장 인기많은 top10 추출
## 인기도 기반으로 추출할 때 사용할 수 있을지도
## 모든 데이터에 대해서 가장 인기많은 top_10 반환하기
from collections import Counter

def predict_most_top_k_products(model, dataloader, k=10):
    model.eval()
    all_top_k_indices = []
    
    with torch.no_grad():
        for batch in dataloader:
            x_categorical, x_continuous, _ = batch
            x_categorical = x_categorical.to(device)
            x_continuous = x_continuous.to(device)
            
            outputs = model(x_categorical, x_continuous)
            
            if outputs.dim() == 1:
                outputs = outputs.unsqueeze(1)
            probabilities = F.softmax(outputs, dim=1)
            top_k_prob, top_k_indices = torch.topk(probabilities, k=k, dim=-1)
            
            all_top_k_indices.extend(top_k_indices.cpu().numpy())
            
    return all_top_k_indices

## 모든 데이터에 대해 예측 수행
all_top_k_indices = predict_all_top_k_products(model, valid_dataloader, k=10)
## 예측된 모든 product_id의 빈도 집계
predicted_counts = Counter([idx for sublist in all_top_k_indices for idx in sublist])
## 가장 자주 예측된 상위 10개 product_id 선정
top_10_predicted_ids = predicted_counts.most_common(10)
top_10_predicted_ids = [id_ for id_, count in top_10_predicted_ids]
## product_id의 idx에 대해서 idx2id로 변환하여 원래 id로 변환
top_k_product_ids = [[idx2id[idx.item()] for idx in batch] for batch in top_k_products]


# 유저의 input을 받아서 topk 반환
def prepare_user_product_data(user_product_id, df, categorical_columns, continuous_columns):
    ## 유저가 선택한 product_id 추출
    user_product_data = filtered_data[filtered_data['product_id'] == user_product_id]
    
    ## 카테고리형 및 연속형 특성을 추출
    X_cat = user_product_data[categorical_columns]
    X_cont = user_product_data[continuous_columns]
    
    ## continuous variable 스케일링
    scaler = StandardScaler()
    X_cont_scaled = scaler.fit_transform(X_cont)
    X_cont_scaled = pd.DataFrame(X_cont_scaled, columns=continuous_columns)
    
    return X_cat, X_cont_scaled

## 유저의 product_id입력
user_product_id = 123456
X_cat_user, X_cont_user = prepare_user_product_data(user_product_id, filtered_data, categorical_columns, continuous_columns)

## 특성 데이터를 모델에 입력 가능한 형태로 변환
X_cat_user_tensor = torch.tensor(X_cat_user.values, dtype=torch.long).to(device)
X_cont_user_tensor = torch.tensor(X_cont_user.values, dtype=torch.float).to(device)

## 모델 평가모드
model.eval()

## 유저의 product_id에 대한 예측
with torch.no_grad():
    output = model(X_cat_user_tensor, X_cont_user_tensor)
    probabilities = F.softmax(output, dim=1)
    top_k_prob, top_k_indices = torch.topk(probabilities, k=10, dim=-1)

## 상위 10개 추천 상품의 인덱스를 추출
top_k_product_idxs = top_k_indices.cpu().numpy()[0]
top_k_product_ids = [idx2id[idx] for idx in top_k_product_idxs]

top_k_product_ids = [[idx2id[idx.item()] for idx in batch] for batch in top_k_products]

# top_k_product_ids : topk 10개 반환된 리스트

###########
