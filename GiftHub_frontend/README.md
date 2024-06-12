# test

## Project setup
```
npm install
```

### Compiles and hot-reloads for development
```
npm run serve
```

### Compiles and minifies for production
```
npm run build
```

### Lints and fixes files
```
npm run lint
```

### Customize configuration
See [Configuration Reference](https://cli.vuejs.org/config/).

# TODO
- []pinia 적용
    - []user information 관리
    - []selected item 관리
    - []추천 아이템에 대한 implicit feedback 관리  
- []POST API요청 구현
    - []user information 전달
    - []selected item 전달(선택할 때마다 전달)
    - []추천 아이템에 대한 implicit feedback 전달(선택할 때마다 전달)
- []GET API요청 구현
    - []9개 아이템 호출
    - []CF기반 예측 호출(선택할 때마다 inference를 호출)
    - []CBF기반 예측 호출(선택할 때마다 inference를 호출)
    - []인기도 기반 예측 호출(초기 유저 정보에 따라 1번만 호출)