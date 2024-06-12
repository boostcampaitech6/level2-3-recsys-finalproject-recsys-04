<template>
  <section class="bg-gray-50 text-center">
    <div class="mx-auto max-w-screen-xl px-4 py-32 lg:flex lg:h-screen lg:items-center">
      <div class="mx-auto max-w-xl ">
        <h1 class="text-3xl font-extrabold sm:text-5xl">가격대</h1>
        <div class="flex justify-between">
          <button class="hidden md:flex w-auto h-10 mx-1 justify-center items-center rounded-full border border-gray-200 bg-white dark:bg-gray-700 text-black dark:text-white hover:border-gray-300 dark:hover:border-gray-600"
                      @click="changePriceType(1)" title="1만원 이하">
                  1만원 이하
          </button>
          <button class="hidden md:flex w-auto h-10 mx-1 justify-center items-center rounded-full border border-gray-200 bg-white dark:bg-gray-700 text-black dark:text-white hover:border-gray-300 dark:hover:border-gray-600"
                      @click="changePriceType(12)" title="10만원 이상">
                  10만원 이상
          </button>
        </div>
        <div class="mt-8 flex flex-wrap justify-center gap-4">
          <VueSlider v-model="price" :width="500" :min="10000" :max="100000" :marks="marks" :included="true" @change="addUserInfo" />
        </div>
        <div class="mt-16 sm:text-xl/relaxed">
          <p>선택된 값: {{ price_type }}</p>
        </div>
      </div>
    </div>
    <div class="absolute py-10 inset-x-0 bottom-0 h-40 ...">
          <nav class="flex flex-row flex-nowrap justify-between md:justify-center items-center" aria-label="Pagination">
            <!-- Previous Page Button -->
            <a class="flex w-10 h-10 mr-1 justify-center items-center rounded-full border border-gray-200 bg-white dark:bg-gray-800 text-black dark:text-white hover:border-gray-300 dark:hover:border-gray-600"
            href="/price" title="Previous Page">
                <span class="sr-only">Previous Page</span>
                <svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke-width="1.5"
                    stroke="currentColor" class="block w-5 h-5">
                    <path stroke-linecap="round" stroke-linejoin="round" d="M15.75 19.5L8.25 12l7.5-7.5" />
                </svg>
              </a>
            <!-- Page Buttons (1 to 5) -->
            <a class="hidden md:flex w-10 h-10 mx-1 justify-center items-center rounded-full border border-gray-200 bg-white dark:bg-gray-700 text-black dark:text-white hover:border-gray-300 dark:hover:border-gray-600"
                href="/gender" aria-current="page" title="Page 1">
                1
            </a>
            <a class="hidden md:flex w-10 h-10 mx-1 justify-center items-center rounded-full border border-gray-200 bg-white dark:bg-gray-700 text-black dark:text-white hover:border-gray-300 dark:hover:border-gray-600"
                href="/age" title="Page 2">
                2
            </a>
            <a class="hidden md:flex w-10 h-10 mx-1 justify-center items-center rounded-full border border-gray-200 bg-white dark:bg-gray-700 text-black dark:text-white hover:border-gray-300 dark:hover:border-gray-600"
                href="/color" title="Page 3">
                3
            </a>
            <a class="hover:border-gray-300 dark:hover:border-gray-600 hidden md:flex w-10 h-10 mx-1 justify-center items-center rounded-full border border-black dark:border-white dark:bg-black dark:text-white pointer-events-none"
                href="/price" title="Page 4">
                4
            </a>
            <a class="hidden md:flex w-10 h-10 mx-1 justify-center items-center rounded-full border border-gray-200 bg-white dark:bg-gray-700 text-black dark:text-white hover:border-gray-300 dark:hover:border-gray-600"
                href="/situation" title="Page 5">
                5
            </a>
            <!-- Next Page Button -->
            <a class="flex w-10 h-10 ml-1 justify-center items-center rounded-full border border-gray-200 bg-white dark:bg-gray-800 text-black dark:text-white hover:border-gray-300 dark:hover:border-gray-600"
            href="/situation" title="Next Page">
                <span class="sr-only">Next Page</span>
                <svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke-width="1.5"
                    stroke="currentColor" class="block w-5 h-5">
                    <path stroke-linecap="round" stroke-linejoin="round" d="M8.25 4.5l7.5 7.5-7.5 7.5" />
                </svg>
            </a>
          </nav>
      </div>
  </section>
</template>
<script>
import { watch, computed, defineComponent, ref } from 'vue';
import { userInfoStore } from '../store/index';
import VueSlider from 'vue-3-slider-component';
export default defineComponent({
  components: { VueSlider },
  setup() {
    const store = userInfoStore();
    const price = ref([30000,50000])
    const marks = [10000,30000,50000,70000,100000]
    const price_type = ref(0)

    const addUserInfo = () => {
      // 값이 변경될 때마다 사용자 정보 저장
      store.addUserInfo({ key: 'price_type', value: price_type.value });
    };

    // price 배열이 변경될 때마다 price_type 업데이트
    watch(price, (newPrice, oldPrice) => {
      const firstPrice = newPrice[0];
      const secondPrice = newPrice[1];

      if (firstPrice == 10000 && secondPrice == 30000) {
        price_type.value = 2;
      } else if (firstPrice == 10000 && secondPrice == 50000) {
        price_type.value = 3;
      } else if (firstPrice == 10000 && secondPrice == 70000) {
        price_type.value = 4;
      } else if (firstPrice ==10000 && secondPrice == 100000) {
        price_type.value = 5;
      } else if (firstPrice ==30000 && secondPrice == 50000) {
        price_type.value = 6;
      } else if (firstPrice ==30000 && secondPrice == 70000) {
        price_type.value = 7;
      } else if (firstPrice ==30000 && secondPrice == 100000) {
        price_type.value = 8;
      } else if (firstPrice ==50000 && secondPrice == 70000) {
        price_type.value = 9;
      } else if (firstPrice ==50000 && secondPrice == 100000) {
        price_type.value = 10;
      } else if (firstPrice ==70000 && secondPrice == 100000) {
        price_type.value = 11;
      }
    });

    const changePriceType = (type) => {
      price_type.value = type;
      store.addUserInfo({ key: 'price_type', value: price_type.value });
    };

    return {
      price,
      marks,
      price_type,
      addUserInfo,
      getDataAll: computed(() => store.getDataAll),
      changePriceType,
    };
  },
});
</script>

