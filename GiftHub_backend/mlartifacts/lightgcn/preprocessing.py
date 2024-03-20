# preprocessing.py
import pandas as pd
import numpy as np
import scipy.sparse as sp
import random

class Preprocess:
    def __init__(self, data_path, config):
        self.data = pd.read_csv(data_path, usecols=['user_id', 'product_id','interaction','timestamp'], header=0)
        self.config = config
        self.user_encoder, self.user_decoder, self.num_users = self._encode_user()
        self.item_encoder, self.item_decoder, self.num_items = self._encode_item()
        self.user_item_matrix = self._generate_user_item_matrix()
        self.adjacency_matrix = self._generate_adjacency_matrix()
        self.exist_users = list(self.user_encoder.values())
        self.exist_items = list(self.item_encoder.values())
        self.user_train = self._generate_user_train()

    def _encode_user(self):
        unique_users = self.data['user_id'].unique()
        user_encoder = {user_id: idx for idx, user_id in enumerate(unique_users)}
        user_decoder = {idx: user_id for user_id, idx in user_encoder.items()}
        return user_encoder, user_decoder, len(unique_users)

    def _encode_item(self):
        unique_items = self.data['product_id'].unique()
        item_encoder = {item_id: idx for idx, item_id in enumerate(unique_items)}
        item_decoder = {idx: item_id for item_id, idx in item_encoder.items()}
        return item_encoder, item_decoder, len(unique_items)

    def _generate_user_item_matrix(self):
        rows = self.data['user_id'].map(self.user_encoder)
        cols = self.data['product_id'].map(self.item_encoder)
        values = np.ones(len(self.data))
        user_item_matrix = sp.csr_matrix((values, (rows, cols)), shape=(self.num_users, self.num_items))
        return user_item_matrix

    def _generate_adjacency_matrix(self):
        user_item_matrix = self.user_item_matrix
        item_user_matrix = self.user_item_matrix.transpose()
        zero_user_to_user = sp.csr_matrix((self.num_users, self.num_users))
        zero_item_to_item = sp.csr_matrix((self.num_items, self.num_items))
        upper_block = sp.hstack([zero_user_to_user, user_item_matrix], format='csr')
        lower_block = sp.hstack([item_user_matrix, zero_item_to_item], format='csr')
        adjacency_matrix = sp.vstack([upper_block, lower_block], format='csr')
        return adjacency_matrix

    def _generate_user_train(self):
        user_train = {}
        for _, row in self.data.iterrows():
            user_id = self.user_encoder[row.user_id]
            item_id = self.item_encoder[row.product_id]
            if user_id not in user_train:
                user_train[user_id] = []
            user_train[user_id].append(item_id)
        return user_train

    def sampling(self):
        users = random.sample(self.exist_users, self.config['n_batch'])
        def sample_pos_items_for_u(u, num):
            pos_items = self.user_train[u]
            pos_batch = random.sample(pos_items, num)
            return pos_batch

        def sample_neg_items_for_u(u, num):
            neg_items = list(set(self.exist_items) - set(self.user_train[u]))
            neg_batch = random.sample(neg_items, num)
            return neg_batch

        pos_items, neg_items = [], []
        for user in users:
            pos_items += sample_pos_items_for_u(user, 1)
            neg_items += sample_neg_items_for_u(user, 1)

        return users, pos_items, neg_items
    def encode_session_items(preprocess, session_items):
    # 새로운 사용자 세션의 아이템을 인코딩
        encoded_items = [preprocess.item_encoder[item] for item in session_items if item in preprocess.item_encoder]
        return encoded_items