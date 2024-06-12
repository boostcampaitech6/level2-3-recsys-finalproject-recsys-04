import pandas as pd
import numpy as np
import torch
import torch.nn as nn
from torch.utils.data import Dataset, DataLoader
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder

# data loading
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

## 각 product_id 내에서 카테고리가 선택될 확률 계산
product_category_counts['total_counts'] = product_category_counts.groupby('product_id')['counts'].transform('sum')
product_category_counts['prob'] = product_category_counts['counts'] / product_category_counts['total_counts']

## 각 product_id에 대한 엔트로피를 계산
## -sigma(pi) * log2(pi)
product_category_counts['personality'] = -product_category_counts['prob'] * np.log2(product_category_counts['prob'])
product_entropy = product_category_counts.groupby('product_id')['personality'].sum().reset_index()

## 매핑
mean_entropy = product_entropy['personality'].mean()
df = df.merge(product_entropy, on='product_id', how='left')
df['personality'].fillna(mean_entropy, inplace=True)


# Categorical data Label Encoding
category_cols = ['category_1', 'category_2', 'category_3', 'brand']
label_encoders = {}
for col in category_cols:
    unique_values = df[col].nunique()
    le = LabelEncoder()
    df[col] = le.fit_transform(df[col])
    label_encoders[col] = le

df = df.drop(['product_name','image_url','product_url'], axis=1)


# continuous data Scaling
## 밑에서 한번에 continous에 대해서 scaling을 진행하기 때문에 이 부분은 굳이 안해도 괜찮음.
### scaling관련해서는 코드에 현재 중복이 있을수도 있으니 참고바람.
from sklearn.preprocessing import StandardScaler

s1 = StandardScaler()
s2 = StandardScaler()

s1.fit(df['price'].values.reshape(-1, 1))
s2.fit(df['num_review'].values.reshape(-1, 1))

price = s1.transform(df['price'].values.reshape(-1, 1))
num_review = s2.transform(df['num_review'].values.reshape(-1, 1))
df['price_scaling'] =price
df['review_scaling'] = num_review

# 칼럼에 _scaling 붙은 부분은 제거할 예정
feature_cols = ['brand', 'category_1', 'category_2', 'category_3', 'rating', 'review_scaling', 'price_scaling', 'personality']
target_col = 'product_id'

# id2idx
id2idx = {id: idx for idx, id in enumerate(sorted(df['product_id']))}
idx2id = {idx: id for id, idx in id2idx.items()}
df['product_idx'] = df['product_id'].map(id2idx)

# Feature Selection and DataLoading
## 특성 및 타겟 선택
X = df[['category_1', 'category_2', 'category_3', 'rating', 'review_scaling', 'price_scaling', 'personality']]
y = df['product_idx']

## 데이터 분할
X_train, X_val, y_train, y_val = train_test_split(X, y, test_size=0.2, random_state=42)

# saparate wide and deep
## 이 경우 continuous_features는 price, num_review로 다시 변경
# categorical_features = ['brand', 'category_1', 'category_2', 'category_3']
# continuous_features = ['rating', 'review_scaling', 'price_scaling', 'personality']

# ## StandardScaler for continuous features
# scaler = StandardScaler()
# X_train[continuous_features] = scaler.fit_transform(X_train[continuous_features])
# X_val[continuous_features] = scaler.transform(X_val[continuous_features])


categorical_columns = ['brand','category_1', 'category_2', 'category_3']
continuous_columns = ['rating', 'review_scaling', 'price_scaling', 'personality']

## 데이터 분할과 스케일링
X = df[categorical_columns + continuous_columns]
y = df['product_idx']


# 카테고리형 데이터와 연속형 데이터 분리
X_categorical = X[categorical_columns]
X_continuous = X[continuous_columns]

# feature값 스케일링
## 여기서도 한 번 더 스케일링을 진행하는데, 다시 확인해볼 필요가 있음.
scaler = StandardScaler()
X_continuous_scaled = scaler.fit_transform(X_continuous)
X_continuous_scaled = pd.DataFrame(X_continuous_scaled, columns=continuous_columns)

X_cat_train, X_cat_val, X_cont_train, X_cont_val, y_train, y_val = train_test_split(X_categorical, X_continuous_scaled, y, test_size=0.2, random_state=42)


from torch.utils.data import TensorDataset, DataLoader, Dataset

def dl_data_split(data, test_size=0.2, seed=42):
    X = df[categorical_columns + continuous_columns]
    y = df['product_idx']
    
    X_train, X_valid, y_train, y_valid = train_test_split(
        X, y, test_size=test_size, random_state=seed, shuffle=True
    )
    
    # 연속형 데이터 스케일링
    scaler = StandardScaler()
    X_train[continuous_columns] = scaler.fit_transform(X_train[continuous_columns])
    X_valid[continuous_columns] = scaler.transform(X_valid[continuous_columns])
    
    return X_train, X_valid, y_train, y_valid


X_train, X_valid, y_train, y_valid = dl_data_split(df)

# DataLoader
## 기본제공되는 TensorDataset은 categorical과 continuous를 나누어서 받지 못함. 
## 따라서 customdataset이 필요
class Cat_Con_Dataset(Dataset):
    def __init__(self, X, y):
        self.X_cat = torch.tensor(X[categorical_columns].values, dtype=torch.long)
        self.X_cont = torch.tensor(X[continuous_columns].values, dtype=torch.float)
        self.y = torch.tensor(y.values, dtype=torch.long)

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


# wide deep model constructure
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
            nn.Linear(mlp_dims[-1], 1)
        )

    def forward(self, x_categorical, x_continuous):
        x_embedded = [embedding(x_categorical[:, i]) for i, embedding in enumerate(self.categorical_embedding)]
        x_embedded = torch.cat(x_embedded, dim=1)
        x_total = torch.cat([x_embedded, x_continuous], dim=1)
        x_linear = self.continuous_linear(x_continuous)
        x_mlp = self.mlp(x_total)
        output = x_linear + x_mlp
        return output.squeeze(1)


# 모델 초기화
## 각각 field_dims를 지정해줘야함.
categorical_field_dims = [df['brand'].nunique(), df['category_1'].nunique(), df['category_2'].nunique(), df['category_3'].nunique()]
continuous_field_dims = ['rating', 'personality', 'price_scaling', 'review_scaling']
model = WideAndDeepModel(categorical_field_dims, 
                         continuous_field_dims, 
                         embed_dim=128, mlp_dims=[128, 64,32], 
                         dropout=0.1).to(torch.device('cuda' if torch.cuda.is_available() else 'cpu'))

# 학습을 위한 metric, optimizer 지정
optimizer = torch.optim.Adam(model.parameters(), lr=0.001, weight_decay=1e-5)
criterion = nn.CrossEntropyLoss()

# GPU 사용 설정
device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
model.to(device)

import wandb

def rmse(y, pred):
    mse = torch.mean((y - pred) ** 2)
    return torch.sqrt(mse)


# wandb.init(project="gift_wdn")

# wandb.watch(model, criterion, log="all", log_freq=10)

epochs = 30

# train
for epoch in range(epochs):
    model.train()  # train mode
    total_loss = 0
    total_rmse = 0

    for batch in train_dataloader:
        optimizer.zero_grad()  

        x_categorical, x_continuous, labels = batch
        x_categorical, x_continuous, labels = x_categorical.to(device), x_continuous.to(device), labels.to(device)

        outputs = model(x_categorical, x_continuous)
        loss = criterion(outputs, labels.float())
        rmse_val = rmse(labels.float(), outputs)


        loss.backward()  
        optimizer.step()  
        total_loss += loss.item() 
        total_rmse += rmse_val.item()

    avg_loss = total_loss / len(train_dataloader)
    avg_rmse = total_rmse / len(train_dataloader)
    
    # wandb.log({'epoch': epoch + 1, 'loss': avg_loss, 'rmse': avg_rmse})
    print(f'Epoch {epoch+1}/{epochs}, Loss: {avg_loss}, RMSE: {avg_rmse}')


# recommendation
## 이 부분은 현재 수정 중에 있음(03.10~)
import torch.nn.functional as F

# 모델의 예측 함수 정의
def predict_top_k_products(model, x_categorical, x_continuous, k=10):
    """
    모델을 사용하여 상위 k개의 product_id를 예측하는 함수
    
    Parameters:
    model (torch.nn.Module): 학습된 모델
    x_categorical (torch.Tensor): 카테고리형 특성 데이터
    x_continuous (torch.Tensor): 연속형 특성 데이터
    k (int): 반환할 상위 product_id의 개수

    Returns:
    torch.Tensor: 상위 k개의 product_id에 대한 인덱스
    """
    # 모델을 평가 모드로 설정
    model.eval()
    
    with torch.no_grad():
        # 데이터를 모델에 통과시키기
        outputs = model(x_categorical, x_continuous)
        print(outputs)
        
        if outputs.dim() == 1:
            outputs = outputs.unsqueeze(1)
        # Softmax 적용하여 확률 분포 얻기
        probabilities = F.softmax(outputs, dim=1)
        print(probabilities.shape)
        
        
        # 상위 k개의 확률과 해당 인덱스(=product_id)를 얻기
        top_k_prob, top_k_indices = torch.topk(probabilities, k=10, dim=-1)
        
    return top_k_indices

# 예측 실행
# x_categorical과 x_continuous에 대한 데이터 준비가 필요
# 예: x_categorical, x_continuous = 데이터 로딩 로직
# device 설정 후 데이터를 device로 이동

x_categorical = x_categorical.to(device)
x_continuous = x_continuous.to(device)

top_k_products = predict_top_k_products(model, x_categorical, x_continuous, k=5)

print("Top 10 predicted product ids:", top_k_products)