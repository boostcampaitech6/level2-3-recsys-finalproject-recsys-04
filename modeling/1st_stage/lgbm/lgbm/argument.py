import argparse


def parse_args():
    parser = argparse.ArgumentParser()

    parser.add_argument("--seed", default=42, type=int, help="seed")
    parser.add_argument("--device", default="gpu", type=str, help="cpu or gpu")
    
    
    # 경로
    parser.add_argument("--data_dir", default="", type=str, help="data directory") 
    parser.add_argument("--asset_dir", default="asset/", type=str, help="data directory")
    parser.add_argument("--model_dir", default="models/", type=str, help="model directory") 
    parser.add_argument("--output_dir", default="outputs/", type=str, help="output directory") 
    parser.add_argument("--model_name", default="best_model.pt", type=str, help="model file name") 
  
    # 모델 선언
    parser.add_argument("--model", default="lgbm", choices=["lgbm"], type=str, help="model select")

    # lgbm 
    parser.add_argument("--n_estimators", default=100, type=int, help="number of epochs")
    parser.add_argument("--learning_rate", default=0.01, type=float, help="nlearning_rate")
    parser.add_argument("--num_leaves", default=4, type=int, help="num_leaves")
    parser.add_argument("--max_depth", default=8, type=int, help="max_depth")

    args = parser.parse_args()

    return args