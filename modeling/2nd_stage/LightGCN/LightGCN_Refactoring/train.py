import torch
from tqdm import tqdm

def train(model, preprocess, optimizer, n_batch, device):
    model.train()
    loss_val = 0
    for _ in tqdm(range(n_batch), desc="Training..."):
        users, pos_items, neg_items = preprocess.sampling()
        users = torch.LongTensor(users).to(device)
        pos_items = torch.LongTensor(pos_items).to(device)
        neg_items = torch.LongTensor(neg_items).to(device)
        optimizer.zero_grad()
        loss = model(users, pos_items, neg_items)
        loss.backward()
        optimizer.step()
        loss_val += loss.item()
    return loss_val / n_batch


def compute_metrics(pred_items, test_items, k):
    """
    예측된 아이템 점수와 실제 테스트 아이템 간의 Recall, Precision, F1 점수를 계산합니다.

    :param pred_items: 예측된 아이템 점수 (사용자 수 x 아이템 수)
    :param test_items: 실제 테스트 아이템 (사용자 수 x 아이템 수), 1과 0으로 이루어진 행렬
    :param k: 상위 k 개의 아이템을 고려
    :return: recall@k, precision@k, F1@k
    """
    _, topk_indices = torch.topk(pred_items, k=k, dim=1)
    topk_preds = torch.zeros_like(pred_items).float()
    topk_preds.scatter_(1, topk_indices, 1)

    # Recall@k: (TP) / (TP + FN)
    tp = (test_items * topk_preds).sum(1)
    recall = (tp / test_items.sum(1)).mean()

    # Precision@k: (TP) / (TP + FP)
    precision = (tp / k).mean()

    # F1 Score: 2 * (precision * recall) / (precision + recall)
    f1 = 2 * precision * recall / (precision + recall + 1e-8)
    f1 = torch.where(torch.isnan(f1), torch.zeros_like(f1), f1)  # NaN 값 처리

    return recall.item(), precision.item(), f1.mean().item()



def evaluate(model, Rtr, Rte, k, device):
    model.eval()
    with torch.no_grad():
        all_embeddings = model.compute_embeddings()
        u_embeddings = all_embeddings[:model.n_users]
        i_embeddings = all_embeddings[model.n_users:]

        scores = torch.matmul(u_embeddings, i_embeddings.T)

        # 실제 테스트 데이터와 비교할 수 있도록 변환
        test_items = torch.FloatTensor(Rte.toarray()).to(device)
        
        recall, precision, f1 = compute_metrics(scores, test_items, k)

    return recall, precision, f1