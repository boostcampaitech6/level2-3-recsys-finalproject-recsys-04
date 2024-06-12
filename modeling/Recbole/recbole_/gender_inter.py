# gender/age에 대한 추론을 진행하기 위한 csv -> inter파일 입니다.

import os
import pandas as pd
'''
# 기존 dataset ml-1m을 바탕으로 칼럼을 만들어줘야 recbole을 사용할 수 있음.
# 먼저 학습에 사용하기 위해 gender를 만든 후, 학습 진행
-> gift는 evaluation용으로 사용. 


ml-1m.inter
|---------------|---------------|--------------|-----------------|
| user_id:token | item_id:token | rating:float | timestamp:float |
|---------------|---------------|--------------|-----------------|
| 1             | 1193          | 5            | 978300760       |
| 1             | 661           | 3            | 978302109       |
|---------------|---------------|--------------|-----------------|

ml-1m.user
|---------------|-----------|--------------|------------------|----------------|
| user_id:token | age:token | gender:token | occupation:token | zip_code:token |
|---------------|-----------|--------------|------------------|----------------|
| 1             | 1193      | F            | 10               | 48067          |
| 2             | 661       | M            | 16               | 70072          |
|---------------|-----------|--------------|------------------|----------------|

ml-1m.item
|---------------|-----------------------|--------------------|-------------------|
| item_id:token | movie_title:token_seq | release_year:token | genre:token_seq   |
|---------------|-----------------------|--------------------|-------------------|
| 1             | Toy Story             | 5                  | Animation Comedy  |
| 2             | Jumanji               | 3                  | Adventure         |
|---------------|-----------------------|--------------------|-------------------|
'''

'''
gender.inter x 6?
|---------------|---------------|--------------|-----------------|
| user_id:token | item_id:token | rating:float | timestamp:float |
|---------------|---------------|--------------|-----------------|
| 1             | 1193          | 5            | 978300760       |
| 1             | 661           | 3            | 978302109       |
|---------------|---------------|--------------|-----------------|
10_m
10_f
2030_m
2030_f
4050_m
4050_f

gender.user x 6?
|---------------|-----------|--------------|------------------|----------------|
| user_id:token | age:token | gender:token | occupation:token | zip_code:token |
|---------------|-----------|--------------|------------------|----------------|
| 1             | 1193      | F            | 10               | 48067          |
| 2             | 661       | M            | 16               | 70072          |
|---------------|-----------|--------------|------------------|----------------|

gender.item
|---------------|-----------------------|--------------------|-------------------|
| item_id:token | movie_title:token_seq | release_year:token | genre:token_seq   |
|---------------|-----------------------|--------------------|-------------------|
| 1             | Toy Story             | 5                  | Animation Comedy  |
| 2             | Jumanji               | 3                  | Adventure         |
|---------------|-----------------------|--------------------|-------------------|
'''

# 현재 위치 : /home/siyun/ephemeral/code
# gift_target_dir = os.path.join(os.getcwd(), "gender_inf")
# gender_target_dir = os.path.join(os.getcwd(), "gender_train")


# 파일 경로 설정
gift_data_path = '/home/siyun/ephemeral/data/gift_group.csv'
gender_data_path = '/home/siyun/ephemeral/data/gender.csv'


gift_target_dir = os.path.join(os.getcwd(), "gender_inf")
gender_target_dir = os.path.join(os.getcwd(), "gender_train")

os.makedirs(gender_target_dir, exist_ok=True)
os.makedirs(gift_target_dir, exist_ok=True)

# gift 데이터 로드, gender 데이터 로드
gift_df = pd.read_csv(gift_data_path)
gender_df = pd.read_csv(gender_data_path)



# .user 파일 생성
## 사용자(성별 및 연령대 그룹) 데이터 생성
### 사용안하면 그대로 둬도 괜찮음. 어차피 inter에 user의 정보를 다 넣기 때문에 사용하지 않아도 괜찮음.
# user_data = {
#     'user_id:token': range(1,7),
#     'group:token': ['2030대_여성', '4050대_여성', '10대_여성', '2030대_남성', '4050대_남성', '10대_남성']
# }

# gift_user_df = pd.DataFrame(user_data)
# gender_user_df = pd.DataFrame(user_data)


# gift_user_df.to_csv(gift_target_dir + '/gender_inf.user', index=False, sep='\t')
# gender_user_df.to_csv(gender_target_dir + '/gender_train.user', index=False, sep='\t')



# .item 파일 생성
def create_item_df(df):
    item_df = df[['product_id', 'product_name', 'brand', 'category_1', 'category_2', 'category_3', 'price']].drop_duplicates()
    item_df.rename(columns={
        'product_id':'item_id:token', 
        'product_name':'name:token_seq', 
        'brand':'brand:token_seq', 
        'category_1':'category_1:token_seq', 
        'category_2': 'category_2:token_seq', 
        'category_3': 'category_3:token_seq', 
        'price': 'price:float'}, inplace=True)
    return item_df


gift_item_df = create_item_df(gift_df)
gender_item_df = create_item_df(gender_df)


gift_item_df.to_csv(gift_target_dir + '/gender_inf.item', index=False, sep='\t')
gender_item_df.to_csv(gender_target_dir + '/gender_train.item', index=False, sep='\t')



# .inter 파일 생성
gift_inter_df = gift_df[['product_id', 'label:float', 'rating']]
gender_inter_df = gender_df[['product_id', 'label:float', 'rating']]

gift_inter_df.rename(columns={'product_id': 'item_id:token', 'rating': 'rating:float'}, inplace=True)
gender_inter_df.rename(columns={'product_id': 'item_id:token', 'rating': 'rating:float'}, inplace=True)

# 모든 상호작용 데이터를 하나의 파일로 저장

# gift_inter_df.to_csv(gift_target_dir + '/gender_inf.inter', index=False, sep='\t')
# gender_inter_df.to_csv(gender_target_dir + '/gender_train.inter', index=False, sep='\t')

gift_inter_df.to_csv(os.path.join(gift_target_dir, 'gender_inf.inter'), index=False, sep='\t')
gender_inter_df.to_csv(os.path.join(gender_target_dir, 'gender_train.inter'), index=False, sep='\t')

print('Done! Successfully created .inter, .user, and .item files for RecBole.')
