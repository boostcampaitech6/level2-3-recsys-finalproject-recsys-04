import json
import math
import os
import random

import numpy as np
import pandas as pd
import torch

def set_seed(seed):
    random.seed(seed)
    os.environ["PYTHONHASHSEED"] = str(seed)
    np.random.seed(seed)
    torch.manual_seed(seed)
    torch.cuda.manual_seed(seed)
    torch.cuda.manual_seed_all(seed)
    # some cudnn methods can be random even after fixing the seed
    # unless you tell it to be deterministic
    torch.backends.cudnn.deterministic = True

def check_path(path):
    if not os.path.exists(path):
        os.makedirs(path)
        print(f"{path} created")

def recall_at_k(ground_truth, predicted_items, k=10):
    """
    Calculate Recall@k
    Parameters:
        ground_truth (dict): 실제 사용자 평가 데이터. {userid: [itemid1, itemid2, ...]}
        predicted_items (dict): 모델이 예측한 아이템 목록. {userid: [predicted_itemid1, predicted_itemid2, ...]}
        k (int): 상위 k개의 예측 아이템을 사용하여 Recall 계산
    Returns:
        recall (float): Recall@k
    """
    total_recall = 0
    total_users = len(ground_truth)

    for user_id, true_items in ground_truth.items():
        predicted = predicted_items.get(user_id, [])[:k]
        true_positives = len(set(predicted) & set(true_items))
        total_recall += true_positives / len(true_items) if len(true_items) > 0 else 0

    recall = total_recall / total_users
    return recall
