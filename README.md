
### Recsys-04 파이팅해야조
# 🎁GiftHub
![image](https://github.com/boostcampaitech6/level2-3-recsys-finalproject-recsys-04/assets/8871767/b681984d-70bf-4587-b49e-067ed7a9b243)
## 프로젝트 소개
![image](https://github.com/boostcampaitech6/level2-3-recsys-finalproject-recsys-04/assets/8871767/a7facf5b-bc15-4225-a24d-df775117000d)
- 개인화 맞춤 선물 추천 프로젝트입니다.
- 선물 받을 사람이 좋아할만한 선물을 추천드립니다!

## 서비스 제공 과정
![image](https://github.com/boostcampaitech6/level2-3-recsys-finalproject-recsys-04/assets/8871767/cbf2ffab-8206-46d1-9807-d6fba4cf2857)
1. 선물할 사람의 연령, 성별, 선물 가격대, 개성, 선물하는 상황 등을 고려하여 선물 후보군을 선정합니다.
2. 추천된 후보군에서 대상자가 구매할 가능성이 높은 상품을 선택하면, 이를 바탕으로 선물 후보 20개를 추천합니다.

## 추천 모델 아키텍처
![image](https://github.com/boostcampaitech6/level2-3-recsys-finalproject-recsys-04/assets/8871767/88ed5236-eea4-4de6-8881-a3fcced9eb16)
- `Stage 1` : 유저 정보를 고려한 아이템에 대해 필터링 하여 트리 계열 예측모델로 추천 후보군을 선정했습니다.
- `Stage 2` : 다양한 아이템을 추천하고자 아이템 기반 협업 필터링, 유저기반 협업 필터링 결과를 반환합니다.

## S/W 아키텍처
  ![image](https://github.com/boostcampaitech6/level2-3-recsys-finalproject-recsys-04/assets/8871767/f8ac4cc9-2671-4256-a635-8b07a5a5b43d)
- 시스템은 크게 `프론트엔드`, `백엔드`, `데이터베이스`, `모델 관리 및 서빙` **4가지 주요 영역**으로 설계되었습니다.

## 데이터베이스 ERD
![image](https://github.com/boostcampaitech6/level2-3-recsys-finalproject-recsys-04/assets/8871767/1dcef64b-eb18-4d7b-a6e7-3f66d5457d5d)
- 유저 정보인 user테이블과 상품 정보인 product테이블 기준으로 유저 상호작용 데이터를 1:N 정규화를 진행했습니다.
- user테이블은 user_id를 기준으로 고유값을 가지고, product테이블은 product_id를 기준으로 고유값을 가집니다.


## 프로젝트 타임라인
![image](https://github.com/boostcampaitech6/level2-3-recsys-finalproject-recsys-04/assets/8871767/bbc95736-5c64-4a6f-b223-88dd04d3b143)

## 팀원 및 역할
| [김세훈](https://github.com/warpfence) | [김시윤](https://github.com/tldbs5026) | [문찬우](https://github.com/chanwoomoon) | [배건우](https://github.com/gunwoof) | [이승준](https://github.com/llseungjun) |
| :------: |  :------: | :------: | :------: | :------: |
| [<img src="https://avatars.githubusercontent.com/u/8871767?v=4" height=150 width=150>](https://github.com/warpfence) | [<img src="https://avatars.githubusercontent.com/u/68991530?v=4" height=150 width=150> ](https://github.com/tldbs5026) | [<img src="https://avatars.githubusercontent.com/u/95879995?v=4" height=150 width=150> ](https://github.com/chanwoomoon) | [<img src="https://avatars.githubusercontent.com/u/83867930?v=4" height=150 width=150>](https://github.com/gunwoof) | [<img src="https://avatars.githubusercontent.com/u/133944361?v=4" height=150 width=150>](https://github.com/llseungjun) |
