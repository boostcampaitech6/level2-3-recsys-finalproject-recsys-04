import os
import sys
import random

import pymysql
import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split

from .logger import get_logger, logging_conf

sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(__file__)))) + '/Feature_Engineering')
#import .feature_engineering as fe

logger = get_logger(logging_conf)

class Preprocess:
    def __init__(self, argument):
        self.argument = argument
        self.train_data = None
        self.test_data = None
        self.all_data = None

    def __data_filtering(self, df: pd.DataFrame) -> pd.DataFrame: 
        filtered_df = pd.DataFrame()
        for col1 in df['category_1'].unique():
            # 특정 category_1 값에 해당하는 행들만 선택
            filtered_df1 = df[df['category_1'] == col1]
    
            # category_1에 대한 price 통계 계산
            # mean_price1 = filtered_df1['price'].mean()
            # std_price1 = filtered_df1['price'].std()
    
            # 결과 출력
            # print(f"len : {len(filtered_df1)} || Category_1: {col1} || 평균 가격: {int(mean_price1)} || 표준 편차: {std_price1:.2f} || Q_0.3: {int(filtered_df1['price'].quantile(0.3))} || Q_0.5: {int(filtered_df1['price'].median())} || Q_0.9: {int(filtered_df1['price'].quantile(0.95))}")
            # print(f"Q 0.3보다 낮은 row의 개수 : {len(filtered_df1[filtered_df1['price'] < filtered_df1['price'].quantile(0.3)])} 의 비율 : {len(filtered_df1[filtered_df1['price'] < filtered_df1['price'].quantile(0.3)]) / len(df)}")
            # category_2의 unique 값에 대해 반복
            for col2 in filtered_df1['category_2'].unique():
                # 특정 category_2 값에 해당하는 행들만 선택
                filtered_df2 = filtered_df1[filtered_df1['category_2'] == col2]

                # category_2에 대한 price 통계 계산
                mean_price2 = filtered_df2['price'].mean()
                std_price2 = filtered_df2['price'].std()
        
                # 각 카테고리1의 하위 카테고리인 카테고리2의 quantile 0.3 이하를 제거 
                q_3 = filtered_df2['price'].quantile(0.3) 
                filtered_q3 = filtered_df2[filtered_df2['price'] > q_3]
                filtered_df = pd.concat([filtered_df, filtered_q3])
        return filtered_df
    def __data_sampling(self, df: pd.DataFrame) -> pd.DataFrame: 
        # 카테고리1 별 비율 계산
        cat1_ratios = df['category_1'].value_counts(normalize=True)

        final_sample_df = pd.DataFrame()
        total_samples = 30000

        # 카테고리1 루프
        for cat1, cat1_ratio in cat1_ratios.items():
            cat1_df = df[df['category_1'] == cat1]
            # print(cat1_ratio)
    
            # 카테고리1의 비율에 따라 할당할 샘플 수 계산 (카테고리1의 비율)
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
                
        # 최종 샘플링 길이 조절
        if len(final_sample_df) > total_samples:
            final_sample_df = final_sample_df.sample(n=total_samples)
        return final_sample_df
    def __data_processing(self, df: pd.DataFrame) -> pd.DataFrame:
        df= pd.get_dummies(df, columns=['category_1', 'category_2', 'category_3'])

        unique_product_ids = np.unique(df['product_id']).tolist()

        # id2idx: 각 product_id를 연속적인 정수 인덱스로 매핑
        id2idx = {product_id: idx for idx, product_id in enumerate(unique_product_ids)}

        df['mapped_product_id'] = df['product_id'].apply(lambda x: id2idx[x])

        # argument에 columns정보 추가
        features_col = list(df.drop(['product_id','mapped_product_id', 'product_name', 'brand', 'image_url', 'product_url'],axis=1).columns)
        targets_col = ['mapped_product_id']
        setattr(self.argument, 'features_col', features_col)
        setattr(self.argument, 'targets_col', targets_col)
        return df
    
    
    # db에서 실제로 받아오고 ndarray로 출력
    def load_data_from_file(self) -> pd.DataFrame:  
        # db연결
        db_connect = pymysql.connect(
            user="recsys4",
            password="recsys1234",
            host="223.130.160.153",
            port=2306,
            database="gifthub"
        )

        # db에서 데이터 가져오기
        df = pd.read_sql("SELECT * FROM rawdata",db_connect)
        db_connect.close()

        # feature engineering 추가 + processiong
        #df = __feature_engineering(df)
        df = self.__data_filtering(df)
        df = self.__data_sampling(df)
        df = self.__data_processing(df)
        
        return df
    
    # none이었던 self.train_data와 self.test_data에 정의
    def load_train_data(self,df) -> None:  
        self.train_data = self.train_test_split(df)['train']
    def load_test_data(self,df) -> None:  
        self.test_data = self.train_test_split(df)['test']
    def load_all_data(self,df) -> None: 
        self.all_data = df
    # train.py에서 data반환
    def get_all_data(self) -> pd.DataFrame:  
        return self.all_data

'''
class preprocess
def __init__(self, args):
    -self.args = args
    -self.train_data = None
    -self.test_data = None

def get_train_data(self) -> pd.DataFrame:  train data 반환(default self.train data=none)
    return self.train_data
def get_test_data(self) -> pd.DataFrame:  test data 반환(default self.test data=none)
    return self.test_data
def split_data(self, df) -> dic:  train과 valis나눈 data 반환

def __feature_engineering(self, df: pd.DataFrame) -> pd.DataFrame:  feature_engineering 추가
def __preprocessing(self, df: pd.DataFrame, is_train: bool = True) -> pd.DataFrame:  data processing

def load_data_from_file(self, file_name: str, is_train: bool = True) -> pd.DataFrame:  split_data후에 실제 데이터를 받아서 dataframe으로 각각 반환
    -데이터베이스에서 가져와야함
def load_train_data(self, file_name: str) -> None:  none이었던 self.train_data에 정의
    -self.train_data = load_data_from_file()
def load_test_data(self, file_name: str) -> None:  none이었던 self.test_data에 정의
    -self.test_data = load_data_from_file()
'''

