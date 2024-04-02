
![Django](https://img.shields.io/badge/django-%23092E20.svg?style=for-the-badge&logo=django&logoColor=white)

## Django Backend 
- Django REST API Framework를 사용하여 데이터 처리에 관한 모든 서비스를 제공합니다.

## Functional definition
### 1. Front-End API 기능 정의
- 사용자 요청에 의한 상호작용 데이터에 대해 관리하고 서비스를 제공합니다.

| Method | URI | Description | Input | Output |
| :------: |  :------: | :------: | :------: | :------: |
| GET | api/user/matched-items/{user_id}/ | 유저 상호작용을 위한 아이템을 전달합니다. | user_id | product_id<br/>image_url |
| GET | api/user/items-prediction/{user_id}/ | 최종 선물을 추천합니다.(LGBM) | user_id | product_id<br/>image_url |
| GET | api/amazon/items-select/ | 유저 상호작용을 위한 아이템을 전달합니다. |  | product_id<br/>product_name<br/>image_url |
| GET | api/amazon/items-prediction/bert4rec/{user_id}/ | 최종 선물을 추천합니다.(BERT4Rec) | user_id | product_id<br/>product_name<br/>image_url |
| GET | api/amazon/items-prediction/ease/{user_id}/ | 최종 선물을 추천합니다.(EASE) | user_id | product_id<br/>product_name<br/>image_url |
| GET | api/amazon/items-prediction/lightgcn/{user_id}/ | 최종 선물을 추천합니다.(LGCN) | user_id | product_id<br/>product_name<br/>image_url |
| POST | api/user/ | 유저 데이터를 생성합니다. | sex<br/>age<br/>price_type<br/>personality<br/>category_1 | user_id<br/>sex<br/>age<br/>price_type<br/>personality<br/>category_1<br/>timestamp |
| POST | api/user/interaction/ | 유저 상호작용 데이터를 생성합니다.(interaction) | user_id<br/>product_id |  |
| POST | api/user/like/ | 유저 상호작용 데이터를 생성합니다.(like) | user_id<br/>product_id |  |
| POST | api/amazon/user/interaction/ | 유저 상호작용 데이터를 생성합니다.(interaction) | user_id<br/>product_id |  |
| POST | api/amazon/user/like/ | 유저 상호작용 데이터를 생성합니다.(like) | user_id<br/>product_id |  |
| DELETE | api/user/interaction/ | 유저 상호작용 데이터를 삭제합니다.(interaction) | user_id<br/>product_id |  |
| DELETE | api/user/like/ | 유저 상호작용 데이터를 삭제합니다.(like) | user_id<br/>product_id |  |
| DELETE | api/amazon/user/interaction/ | 유저 상호작용 데이터를 삭제합니다.(interaction) | user_id<br/>product_id |  |
| DELETE | api/amazon/user/like/ | 유저 상호작용 데이터를 삭제합니다.(like) | user_id<br/>product_id |  |

### 2. 데이터베이스 입출력
- Django는 다양한 데이터베이스 서버를 지원하며 본 프로젝트에서는 MariaDB를 연결하여 사용합니다.
- `Django ORM을 이용한 데이터 입출력` :  데이터를 객체로 다루며 Django 모델을 통해 데이터베이스 테이블을 정의하고, 데이터를 생성, 조회, 수정, 삭제합니다.
- `Database Connect SQL쿼리 접근` : Django ORM으로 처리하기 어려운 복잡한 쿼리나 특정 데이터베이스 기능을 최대한 활용하기 위해 사용합니다.

## Directory Structure
```
GiftHub_backend
 ┣ GiftHubApp
 ┃ ┣ api
 ┃ ┃ ┣ requests
 ┃ ┃ ┃ ┣ __init__.py
 ┃ ┃ ┃ ┣ model_request.py
 ┃ ┃ ┃ ┗ request.py
 ┃ ┃ ┗ responses
 ┃ ┃ ┃ ┣ amazon
 ┃ ┃ ┃ ┃ ┣ __init__.py
 ┃ ┃ ┃ ┃ ┗ views.py
 ┃ ┃ ┃ ┣ test
 ┃ ┃ ┃ ┃ ┣ __init__.py
 ┃ ┃ ┃ ┃ ┗ views.py
 ┃ ┃ ┃ ┗ user
 ┃ ┃ ┃ ┃ ┣ __init__.py
 ┃ ┃ ┃ ┃ ┗ views.py
 ┃ ┣ database
 ┃ ┃ ┣ __init__.py
 ┃ ┃ ┣ models.py
 ┃ ┃ ┣ serializers.py
 ┃ ┃ ┗ sql_executor.py
 ┃ ┣ migrations
 ┃ ┃ ┣ 0001_initial.py
 ┃ ┃ ┗ __init__.py
 ┃ ┣ __init__.py
 ┃ ┣ admin.py
 ┃ ┣ apps.py
 ┃ ┣ models.py
 ┃ ┣ open_api_params.py
 ┃ ┣ routers.py
 ┃ ┣ tests.py
 ┃ ┣ urls.py
 ┃ ┣ utils.py
 ┃ ┗ views.py
 ┣ GiftHubProject
 ┃ ┣ __init__.py
 ┃ ┣ asgi.py
 ┃ ┣ settings.py
 ┃ ┣ urls.py
 ┃ ┗ wsgi.py
 ┣ Dockerfile
 ┣ README.md
 ┣ deploy.sh
 ┣ docker-compose.yml
 ┣ manage.py
 ┗ requirements.txt
```
## Docker 설치
1. 작성된 Dockerfile을 빌드하여 이미지를 생성합니다.
2. 빌드된 이미지를 컨테이너를 생성하여 실행합니다.

### 도커 빌드
```bash
docker build --no-cache . --tag django:${VERSION}
```
### 컨테이너 생성 및 실행
```bash
docker run -dit -p 8000:8000 --name django django:${VERSION}
```

## 버전 업데이트 및 배포
- 새로운 기능이 추가되어 버전이 업데이트 된다면 shell 파일을 실행하여 배포합니다.
### 배포 파일 실행
```bash
bash deploy.sh
```
