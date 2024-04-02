![FastAPI](https://img.shields.io/badge/FastAPI-005571?style=for-the-badge&logo=fastapi)

## FastAPI Model Serving
- FastAPI Framework를 모델 추론 결과에 관한 서비스를 제공합니다.

## Functional definition
### 1. Model Serving API 기능 정의
- 사용자 요청에 의한 상호작용 데이터에 대해 관리하고 서비스를 제공합니다.

| Method | URI | Description | Input | Output |
| :------: |  :------: | :------: | :------: | :------: |
| POST | /naver/model/lgbm | LGBM 모델을 예측합니다. | columns[list]<br/>rows[list]<br/>product_id | product_id[list] |
| POST | /amazon/model/bert4rec | BERT4Rec 모델을 예측합니다. | matrix[list] | product_id[list] |
| POST | /amazon/model/ease | EASE 모델을 예측합니다. | columns[list]<br/>rows[list] | product_id[list] |
| POST | /amazon/model/lightgcn | LGCN 모델을 예측합니다. | matrix[list] | product_id[list] |

### 2. Model Loading
- MLflow로 관리되는 모델 버전을 다운로드하여 결과를 서빙합니다.
- 모델 버전은 Config 파일로 관리하며 필요시 다운로드 받을 수 있습니다.

## Directory Structure
```
GiftHub_serving
 ┣ models
 ┃ ┣ BERT4Rec
 ┃ ┃ ┣ BERT4Rec.py
 ┃ ┃ ┣ __init__.py
 ┃ ┃ ┣ item.json
 ┃ ┣ EASE
 ┃ ┃ ┣ src
 ┃ ┃ ┃ ┣ EASE.py
 ┃ ┃ ┃ ┣ __init__.py
 ┃ ┃ ┃ ┗ utils.py
 ┃ ┣ category_proba
 ┃ ┣ lightgcn
 ┃ ┃ ┣ __init__.py
 ┃ ┃ ┣ modeling.py
 ┃ ┃ ┣ preprocessing.py
 ┃ ┃ ┣ recommend.py
 ┃ ┗ __init__.py
 ┣ Dockerfile
 ┣ README.md
 ┣ api.py
 ┣ base.py
 ┣ config.py
 ┣ deploy.sh
 ┣ main.py
 ┣ model_loader.py
 ┣ model_serving.py
 ┣ requirements.txt
 ┣ setting.env
 ┗ utils.py
```
## Docker 설치
1. 작성된 Dockerfile을 빌드하여 이미지를 생성합니다.
2. 빌드된 이미지를 컨테이너를 생성하여 실행합니다.

### 도커 빌드
```bash
docker build --no-cache . --tag fastapi:${VERSION}
```
### 컨테이너 생성 및 실행
```bash
docker run --gpus all -dit -v /home/ksh/camp/level2-3-recsys-finalproject-recsys-04/GiftHub_serving:/home/GiftHub_serving -p 8011:8011 --name fastapi fastapi:${VERSION}
```

## 버전 업데이트 및 배포
- 새로운 기능이 추가되어 버전이 업데이트 된다면 shell 파일을 실행하여 배포합니다.
### 배포 파일 실행
```bash
bash deploy.sh
```
