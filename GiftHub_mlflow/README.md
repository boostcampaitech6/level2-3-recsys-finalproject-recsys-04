## mlflow 서버 세팅
- 실험관리 및 모델 서빙을 위해 mlflow를 사용합니다.

### 1. mlflow 설치
- 원하는 위치에 디렉토리 설정하고 Dockerfile을 빌드합니다.
- 컨테이너 볼륨 마운트를 이용하여 디렉토리를 공유 하여 데이터를 백업합니다.

#### 디렉토리 설정
```bash
cd ${DIR}
```
#### 도커 빌드
```bash
docker build --no-cache . --tag mlflow:${VERSION}
```
#### 컨테이너 생성 및 실행
```bash
docker run -dit -v ${DIR}:/home/mlflow -p 8010:8010 --name mlflow mlflow:${VERSION}
```
---
#### 도커 및 컨테이너 배포 Script
```bash
VERSION=1.0.0
cd /home/ksh/level2-3-recsys-finalproject-recsys-04/GiftHub_mlflow
docker build --no-cache . --tag mlflow:${VERSION}
docker stop mlflow
docker rm mlflow
docker run -dit -v /home/ksh/level2-3-recsys-finalproject-recsys-04/GiftHub_mlflow:/home/mlflow -p 8010:8010 --name mlflow mlflow:${VERSION}

```