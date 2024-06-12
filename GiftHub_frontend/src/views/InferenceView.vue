<template>
    <section class="text-gray-600 body-font">
      <div v-if ="isLoading" class="flex justify-center items-center h-screen">
        <div class="rounded-full h-20 w-20 bg-violet-800 animate-ping"></div>
      </div>
      <div v-if="modalCheck%2 == 1" class="black-bg container px-5 py-10 mx-auto z-40">
        <div class="white-bg lg:w-4/5 mx-auto flex flex-wrap">
          <img alt="ecommerce" class="lg:w-1/2 w-full lg:h-auto h-64 object-cover object-center rounded" :src="amazonProductDetail.image_url">
          <div class="lg:w-1/2 w-full lg:pl-10 lg:py-6 mt-6 lg:mt-0">
            <h2 class="text-sm title-font text-gray-500 tracking-widest">BRAND NAME</h2>
            <h1 class="text-gray-900 text-3xl title-font font-medium mb-1">{{ amazonProductDetail.product_name }}</h1>
            <div class="flex mb-4">
              <span class="flex items-center">
                <svg fill="currentColor" stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="2" class="w-4 h-4 text-indigo-500" viewBox="0 0 24 24">
                  <path d="M12 2l3.09 6.26L22 9.27l-5 4.87 1.18 6.88L12 17.77l-6.18 3.25L7 14.14 2 9.27l6.91-1.01L12 2z"></path>
                </svg>
                <svg fill="currentColor" stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="2" class="w-4 h-4 text-indigo-500" viewBox="0 0 24 24">
                  <path d="M12 2l3.09 6.26L22 9.27l-5 4.87 1.18 6.88L12 17.77l-6.18 3.25L7 14.14 2 9.27l6.91-1.01L12 2z"></path>
                </svg>
                <svg fill="currentColor" stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="2" class="w-4 h-4 text-indigo-500" viewBox="0 0 24 24">
                  <path d="M12 2l3.09 6.26L22 9.27l-5 4.87 1.18 6.88L12 17.77l-6.18 3.25L7 14.14 2 9.27l6.91-1.01L12 2z"></path>
                </svg>
                <svg fill="currentColor" stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="2" class="w-4 h-4 text-indigo-500" viewBox="0 0 24 24">
                  <path d="M12 2l3.09 6.26L22 9.27l-5 4.87 1.18 6.88L12 17.77l-6.18 3.25L7 14.14 2 9.27l6.91-1.01L12 2z"></path>
                </svg>
                <svg fill="none" stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="2" class="w-4 h-4 text-indigo-500" viewBox="0 0 24 24">
                  <path d="M12 2l3.09 6.26L22 9.27l-5 4.87 1.18 6.88L12 17.77l-6.18 3.25L7 14.14 2 9.27l6.91-1.01L12 2z"></path>
                </svg>
                <span class="text-gray-600 ml-3">4 Reviews</span>
              </span>
              <span class="flex ml-3 pl-3 py-2 border-l-2 border-gray-200 space-x-2s">
                <a class="text-gray-500">
                  <svg fill="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="2" class="w-5 h-5" viewBox="0 0 24 24">
                    <path d="M18 2h-3a5 5 0 00-5 5v3H7v4h3v8h4v-8h3l1-4h-4V7a1 1 0 011-1h3z"></path>
                  </svg>
                </a>
                <a class="text-gray-500">
                  <svg fill="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="2" class="w-5 h-5" viewBox="0 0 24 24">
                    <path d="M23 3a10.9 10.9 0 01-3.14 1.53 4.48 4.48 0 00-7.86 3v1A10.66 10.66 0 013 4s-4 9 5 13a11.64 11.64 0 01-7 2c9 5 20 0 20-11.5a4.5 4.5 0 00-.08-.83A7.72 7.72 0 0023 3z"></path>
                  </svg>
                </a>
                <a class="text-gray-500">
                  <svg fill="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="2" class="w-5 h-5" viewBox="0 0 24 24">
                    <path d="M21 11.5a8.38 8.38 0 01-.9 3.8 8.5 8.5 0 01-7.6 4.7 8.38 8.38 0 01-3.8-.9L3 21l1.9-5.7a8.38 8.38 0 01-.9-3.8 8.5 8.5 0 014.7-7.6 8.38 8.38 0 013.8-.9h.5a8.48 8.48 0 018 8v.5z"></path>
                  </svg>
                </a>
              </span>
            </div>
            <p class="leading-relaxed">Fam locavore kickstarter distillery. Mixtape chillwave tumeric sriracha taximy chia microdosing tilde DIY. XOXO fam indxgo juiceramps cornhole raw denim forage brooklyn. Everyday carry +1 seitan poutine tumeric. Gastropub blue bottle austin listicle pour-over, neutra jean shorts keytar banjo tattooed umami cardigan.</p>
            <div class="flex mt-6 items-center pb-5 border-b-2 border-gray-100 mb-5">
              <div class="flex">
                <span class="mr-3">Color</span>
                <button class="border-2 border-gray-300 rounded-full w-6 h-6 focus:outline-none"></button>
                <button class="border-2 border-gray-300 ml-1 bg-gray-700 rounded-full w-6 h-6 focus:outline-none"></button>
                <button class="border-2 border-gray-300 ml-1 bg-indigo-500 rounded-full w-6 h-6 focus:outline-none"></button>
              </div>
              <div class="flex ml-6 items-center">
                <span class="mr-3">Size</span>
                <div class="relative">
                  <select class="rounded border appearance-none border-gray-300 py-2 focus:outline-none focus:ring-2 focus:ring-indigo-200 focus:border-indigo-500 text-base pl-3 pr-10">
                    <option>SM</option>
                    <option>M</option>
                    <option>L</option>
                    <option>XL</option>
                  </select>
                  <span class="absolute right-0 top-0 h-full w-10 text-center text-gray-600 pointer-events-none flex items-center justify-center">
                    <svg fill="none" stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="2" class="w-4 h-4" viewBox="0 0 24 24">
                      <path d="M6 9l6 6 6-6"></path>
                    </svg>
                  </span>
                </div>
              </div>
            </div>
            <div class="flex">
              <span class="title-font font-medium text-2xl text-gray-900">$58.00</span>
              <button @click="showProductsDetail(amazonProductDetail)" class="flex ml-auto text-white bg-indigo-500 border-0 py-2 px-6 focus:outline-none hover:bg-indigo-600 rounded">나가기</button>
              <button v-if = "!amazonIsClicked.includes(amazonProductDetail.product_id)" @click="handleProductClick(amazonProductDetail,'interaction','amazon')" class="rounded-full w-10 h-10 bg-gray-200 p-0 border-0 inline-flex items-center justify-center text-gray-500 ml-4">
                <svg class="text-red-500"  width="24" height="24" viewBox="0 0 24 24" stroke-width="2" stroke="currentColor" fill="none" stroke-linecap="round" stroke-linejoin="round">  
                    <path stroke="none" d="M0 0h24v24H0z"/>  
                    <rect x="4" y="4" width="16" height="16" rx="2" />
                </svg>
              </button>
              <button v-if = "amazonIsClicked.includes(amazonProductDetail.product_id)" @click="handleProductClick(amazonProductDetail,'interaction','amazon')" class="rounded-full w-10 h-10 bg-gray-200 p-0 border-0 inline-flex items-center justify-center text-gray-500 ml-4">
                <svg class="text-red-500"  width="24" height="24" viewBox="0 0 24 24" stroke-width="2" stroke="currentColor" fill="none" stroke-linecap="round" stroke-linejoin="round">  <path stroke="none" d="M0 0h24v24H0z"/>  
                    <rect x="4" y="4" width="16" height="16" rx="2" />  
                    <path d="M9 12l2 2l4 -4" />
                </svg>
              </button>
            </div>
          </div>
        </div>
      </div>
      <div v-if ="!isLoading" class="container px-5 py-10 mx-auto">
        <div class="flex flex-wrap w-full mb-20">
          <div class="lg:w-1/2 w-full mb-6 lg:mb-0">
            <h1 class="sm:text-3xl text-2xl font-extrabold title-font mb-2 text-gray-900">상대방을 떠올리며 상품을 선택해주세요.</h1>
            <div class="h-1 w-21 bg-indigo-500 rounded"></div>
            <p class="mt-5 lg:w-1/2 w-full font-extrabold leading-relaxed text-gray-500">이를 바탕으로 추천해드릴게요.<br> 1개 이상의 상품에 대해 체크표시를 남겨주세요.</p>
          </div>
          <p v-if = "amazonIsClicked.length!=0" class="lg:w-1/2 w-full leading-relaxed text-gray-500">
            <button @click="getPrediction('amazon','lightgcn'), getPrediction('amazon','ease'), getPrediction('amazon','bert4rec')" class="rounded-md bg-white px-3.5 py-2.5 text-sm font-semibold text-gray-900 shadow-sm hover:bg-gray-100 focus-visible:outline focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-white" style="font-size: 20px;">선물 추천 바로받기</button>
          </p>
        </div>
        <Carousel :items-to-show="2.5" :wrap-around="true" class="flex flex-wrap -m-4">
          <Slide v-for="(item, index) in amazonProductList" :key="index" class="xl:w-1/4 md:w-1/2 p-4">
            <div class="bg-gray-100 p-6 rounded-lg">
              <img @click="showProductsDetail(item)" class="h-40 rounded w-full object-cover object-center mb-6" :src="item.image_url" alt="content">
                <button v-if = "amazonIsClicked.includes(item.product_id)">                
                    <svg class="h-8 w-8 text-red-500 absolute top-4 md:top-9 right-9"  width="24" height="24" viewBox="0 0 24 24" stroke-width="2" stroke="currentColor" fill="none" stroke-linecap="round" stroke-linejoin="round">  <path stroke="none" d="M0 0h24v24H0z"/>  
                        <rect x="4" y="4" width="16" height="16" rx="2" />  
                        <path d="M9 12l2 2l4 -4" />
                    </svg>
                </button>
                <button @click="handleProductClick(item,'interaction','amazon')">
                    <svg class="h-8 w-8 text-red-500 absolute top-4 md:top-9 right-9"  width="24" height="24" viewBox="0 0 24 24" stroke-width="2" stroke="currentColor" fill="none" stroke-linecap="round" stroke-linejoin="round">  
                        <path stroke="none" d="M0 0h24v24H0z"/>  
                        <rect x="4" y="4" width="16" height="16" rx="2" />
                    </svg>
                </button>
                <h3 class="tracking-widest text-indigo-500 text-xs font-medium title-font">{{ item.subtitle }}</h3>
                <h2 class="text-lg text-gray-900 font-medium title-font mb-4">{{ item.product_name }}</h2>
                <p class="leading-relaxed text-base">{{ item.description }}</p>
            </div>
          </Slide>
    
          <template #addons>
            <Navigation />
          </template>
        </Carousel>
        </div>
        <div v-if ="donePredict" class="container px-5 py-10 mx-auto">
          <div class="flex flex-wrap w-full mb-20">
            <div class="lg:w-1/2 w-full mb-6 lg:mb-0">
              <h1 class="sm:text-3xl text-2xl font-extrabold title-font mb-2 text-gray-900">나와 비슷한 고민을 했던 사람들이 구매한 상품</h1>
              <div class="h-1 w-21 bg-indigo-500 rounded"></div>
            </div>
          </div>
          <div class="flex flex-wrap mt-5">
            <div v-for="(item, index) in amazonPredictionList" :key="index" class="xl:w-1/5 md:w-1/2 p-4">
              <div class="bg-gray-100 p-6 rounded-lg">
                <img @click="showProductsDetail(item)" class="h-40 rounded w-full object-cover object-center mb-6" :src="item.image_url" alt="content">
                <h3 class="tracking-widest text-indigo-500 text-xs font-medium title-font">{{ item.subtitle }}</h3>
                <h2 class="text-lg text-gray-900 font-medium title-font mb-4">{{ item.product_name }}</h2>
                <p class="leading-relaxed text-base">{{ item.description }}</p>
              </div>
            </div>
          </div>
        </div>
        <div v-if ="donePredict" class="container px-5 py-10 mx-auto">
          <div class="flex flex-wrap w-full mb-20">
            <div class="lg:w-1/2 w-full mb-6 lg:mb-0">
              <h1 class="sm:text-3xl text-2xl font-extrabold title-font mb-2 text-gray-900">선택하신 상품을 바탕으로 추천된 결과입니다.</h1>
              <div class="h-1 w-21 bg-indigo-500 rounded"></div>
            </div>
          </div>
          <div class="flex flex-wrap mt-5">
            <div v-for="(item, index) in easeAmazonPredictionList.slice(0, 5)" :key="index" class="xl:w-1/5 md:w-1/2 p-4">
              <div class="bg-gray-100 p-6 rounded-lg">
                <img @click="showProductsDetail(item)" class="h-40 rounded w-full object-cover object-center mb-6" :src="item.image_url" alt="content">
                <h3 class="tracking-widest text-indigo-500 text-xs font-medium title-font">{{ item.subtitle }}</h3>
                <h2 class="text-lg text-gray-900 font-medium title-font mb-4">{{ item.product_name }}</h2>
                <p class="leading-relaxed text-base">{{ item.description }}</p>
              </div>
            </div>
          </div>
          <div class="flex flex-wrap mt-5">
            <div v-for="(item, index) in bertAmazonPredictionList.slice(0, 5)" :key="index" class="xl:w-1/5 md:w-1/2 p-4">
              <div class="bg-gray-100 p-6 rounded-lg">
                <img @click="showProductsDetail(item)" class="h-40 rounded w-full object-cover object-center mb-6" :src="item.image_url" alt="content">
                <h3 class="tracking-widest text-indigo-500 text-xs font-medium title-font">{{ item.subtitle }}</h3>
                <h2 class="text-lg text-gray-900 font-medium title-font mb-4">{{ item.product_name }}</h2>
                <p class="leading-relaxed text-base">{{ item.description }}</p>
              </div>
            </div>
          </div>
        </div>
    </section>
    </template>
    
    <script>
    import { Carousel, Navigation, Pagination, Slide } from 'vue3-carousel'
    import { computed, ref, defineComponent, onMounted } from 'vue';
    import { userInfoStore } from '../store/index';
    import axios from 'axios';
    import 'vue3-carousel/dist/carousel.css'
    
    export default defineComponent({
        components: {
            Carousel,
            Slide,
            Pagination,
            Navigation,
        },
        setup() {
            //product
            const amazonProductDetail = ref({});
            const amazonProductList = ref([]);
            const amazonProductListToShow = ref([]);
            const easeAmazonPredictionList = ref([]);
            const bertAmazonPredictionList = ref([]);
            //flag 변수
            const modalCheck = ref(0);
            const amazonIsClicked = ref([]);
            const isLoading = ref(true);
            const donePredict = ref(false); 
            //predict 결과
            const amazonPredictionList = ref([]);
            //store
            const store = userInfoStore();

            //get으로 아마존 상품 27개 가져오기
            const getAmazonList = async () => {
                try {
                    const response = await axios.get(`/api/amazon/items-select`);
                    amazonProductList.value = response.data;
                    store.amazonMatchedItems.value = amazonProductList.value;
                    console.log('amazon productList', amazonProductList.value);
                    setPredictionList();
                } catch (error) {
                    console.error('데이터를 가져오는 중에 오류가 발생했습니다:', error);
                }
            };
            
            //get으로 prediction 결과 10개 가져오기
            const getPrediction = async(data,model) => {
              if(model == 'lightgcn'){
                try {
                    isLoading.value = true;
                    const user_id = store.getDataAll.user_id
                    const response = await axios.get(`/api/amazon/items-prediction/${model}/${user_id}`);
                    amazonPredictionList.value = response.data;
                    console.log('lgcn amazonPredictionList', amazonPredictionList.value);
                    donePredict.value = true;
                    isLoading.value = false;
                } catch (error) {
                    console.error('데이터를 가져오는 중에 오류가 발생했습니다:', error);
                } 
              } else if( model == 'ease'){
                try {
                    isLoading.value = true;
                    const user_id = store.getDataAll.user_id
                    const response = await axios.get(`/api/amazon/items-prediction/${model}/${user_id}`);
                    easeAmazonPredictionList.value = response.data;
                    console.log('user_id',user_id);
                    console.log('ease amazonPredictionList', easeAmazonPredictionList.value);
                    donePredict.value = true;
                    isLoading.value = false;
                } catch (error) {
                    console.error('데이터를 가져오는 중에 오류가 발생했습니다:', error);
                }   
              } else{
                try {
                    isLoading.value = true;
                    const user_id = store.getDataAll.user_id
                    const response = await axios.get(`/api/amazon/items-prediction/${model}/${user_id}`);
                    bertAmazonPredictionList.value = response.data;
                    console.log('bert amazonPredictionList', bertAmazonPredictionList.value);
                    donePredict.value = true;
                    isLoading.value = false;
                } catch (error) {
                    console.error('데이터를 가져오는 중에 오류가 발생했습니다:', error);
                } 
              }
    
            };
    
            //predictionList,amazonPredictionList 초기화 함수
            const setPredictionList = async() => {
                amazonPredictionList.value = [{ image_url: 'https://shop-phinf.pstatic.net/20230308_89/1678249882534ecdzU_JPEG/79385717218304917_1496244196.jpg?type=f480_480' }];
                console.log('amazonPredictionList', amazonPredictionList.value);
            };
    
            //상품 중 고른 상품에 대해 POST와 DELETE 요청을 처리하는 함수
            const handleProductClick = async (product, type, data) => { //type : 'like' or 'interation', data: 'amazon' or 'naver'
                const user_id = store.getDataAll.user_id
                console.log('user_id',user_id);
                if (data == 'amazon'){
                    if (!amazonIsClicked.value.includes(product.product_id)) {
                        try {
                        // POST 요청을 보내는 부분
                        const response = await axios.post(`/api/amazon/user/${type}/`, {
                            "user_id": user_id,
                            "product_id": product.product_id,
                        });
                        amazonIsClicked.value.push(product.product_id);
                        console.log('amazon POST request successful:',amazonIsClicked.value);
                        } catch (error) {
                        console.error('Error sending POST request:', error);
                        }
                    } else {
                        try {
                        // DELETE 요청을 보내는 부분
                        await axios.delete(`/api/amazon/user/${type}/`, {
                            data: {
                                "user_id": user_id,
                                "product_id": product.product_id,
                            },
                        });
                        amazonIsClicked.value.splice(amazonIsClicked.value.indexOf(product.product_id), 1);
                        console.log('amazon DELETE request successful:',amazonIsClicked.value);
                        } catch (error) {
                        console.error('Error sending DELETE request:', error);
                        }
                    }
                }            
            };
            // 상품 상세 모달창 클릭 여부
            const showProductsDetail = async(item) => {
                modalCheck.value++;
                console.log("modalCheck.value:",modalCheck.value);
                amazonProductDetail.value = item;
                console.log("amazonProductDetail.value:",amazonProductDetail.value);
            };
    
            //9개 이미지 랜더링 hook
            onMounted(async () => {
                // 비동기 작업을 수행하여 시간을 늦출 수 있음, userInfoStore에 post로 user_id를 가져오는데 생기는 지연 시간 때문에 생기는 버그 때문에 추가
                await new Promise(resolve => setTimeout(resolve, 2000));
                
                getAmazonList();
                amazonIsClicked.value =[];
                isLoading.value = false;
                donePredict.value = false; 
            });
    
            return {
            isLoading,
            donePredict,
            modalCheck,
            amazonIsClicked,
            amazonPredictionList,
            amazonProductList,
            easeAmazonPredictionList,
            bertAmazonPredictionList,
            amazonProductListToShow,
            setPredictionList,
            handleProductClick,
            getPrediction,
            showProductsDetail,
            amazonProductDetail,
            };
        }
    });
    </script>
    
    <style>
    .black-bg {
      width: 100%; height:100%;
      background: rgba(0,0,0,0.5);
      position: fixed; padding: 20px;
    }
    .white-bg {
      width: 100%; background: white;
      border-radius: 8px;
      padding: 20px;
    } 
    </style>