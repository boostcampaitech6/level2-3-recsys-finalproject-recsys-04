<template>
  <section class="bg-gray-50 text-center">
    <div class="mx-auto max-w-screen-xl px-4 py-32 lg:flex lg:h-screen lg:items-center">
      <div class="mx-auto max-w-xl ">
        <h1 class="text-3xl font-extrabold sm:text-5xl">선물 받는 사람의 개성</h1>
        <div class="mt-16 flex flex-wrap justify-center gap-4">
          <VueSlider v-model="personality" :width="500" :min="1" :max="100" :height="20" :marks="[1,100]" :interval="1" tooltip="always" :tooltip-formatter="'{value}%'" :clickable="false" :dragOnClick="false" @change="addUserInfo(personality)" />
        </div>
        <div class="mt-8 sm:text-xl/relaxed">
          <p>선택된 값: {{personality}}</p>
        </div>
      </div>
    </div>
    <div class="absolute py-10 inset-x-0 bottom-0 h-40 ...">
          <nav class="flex flex-row flex-nowrap justify-between md:justify-center items-center" aria-label="Pagination">
            <!-- Previous Page Button -->
            <a class="flex w-10 h-10 mr-1 justify-center items-center rounded-full border border-gray-200 bg-white dark:bg-gray-800 text-black dark:text-white hover:border-gray-300 dark:hover:border-gray-600"
            href="/age" title="Previous Page">
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
            <a class="hover:border-gray-300 dark:hover:border-gray-600 hidden md:flex w-10 h-10 mx-1 justify-center items-center rounded-full border border-black dark:border-white dark:bg-black dark:text-white pointer-events-none"
                href="/color" title="Page 3">
                3
            </a>
            <a class="hidden md:flex w-10 h-10 mx-1 justify-center items-center rounded-full border border-gray-200 bg-white dark:bg-gray-700 text-black dark:text-white hover:border-gray-300 dark:hover:border-gray-600"
                href="/price" title="Page 4">
                4
            </a>
            <a class="hidden md:flex w-10 h-10 mx-1 justify-center items-center rounded-full border border-gray-200 bg-white dark:bg-gray-700 text-black dark:text-white hover:border-gray-300 dark:hover:border-gray-600"
                href="/situation" title="Page 5">
                5
            </a>
            <!-- Next Page Button -->
            <a class="flex w-10 h-10 ml-1 justify-center items-center rounded-full border border-gray-200 bg-white dark:bg-gray-800 text-black dark:text-white hover:border-gray-300 dark:hover:border-gray-600"
            href="/price" title="Next Page">
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
import { computed, defineComponent, ref } from 'vue';
import { userInfoStore } from '../store/index';
import VueSlider from 'vue-3-slider-component';

export default defineComponent({
  components: { VueSlider },
  setup() {
    const store = userInfoStore();
    const personality = ref(50);

    const addUserInfo = (e) => {
      store.addUserInfo({ key: 'personality', value: e });
    };

    const routeTo = (path) => {
      // router를 import하여 사용
      store.routeTo(path);
    };

    const postDataToApi = () => {
      const data = store.getDataAll;
      console.log(data);
      store.postData(data);
    };

    const getDataToApi = () => {
      store.getData();
    };

    return {
      personality,
      addUserInfo,
      routeTo,
      postDataToApi,
      getDataToApi,
      getDataAll: computed(() => store.getDataAll),
    };
  }
});

</script>
<!-- <template>
    <h1>선물 받는 사람의 개성</h1>
    <input type="range" min="1" max="100" v-model="personality" @change="addUserInfo(personality)"><br>
    <p>선택된 값: {{ personality }}</p><br>
    <button @click="routeTo('/age')">prev</button>
    <button @click="routeTo('/price')">next</button>
    <br><h1>{{ getDataAll }}</h1>
    <br><button @click="postDataToApi(), getDataToApi()">전송</button>
</template>
<script>
import { computed, defineComponent, ref } from 'vue';
import { userInfoStore } from '../store/index';

export default defineComponent({
  setup() {
    const store = userInfoStore();
    const personality = ref(50);

    const addUserInfo = (e) => {
      store.addUserInfo({ key: 'personality', value: e });
    };

    const routeTo = (path) => {
      // router를 import하여 사용
      store.routeTo(path);
    };

    const postDataToApi = () => {
      const data = store.getDataAll;
      console.log(data);
      store.postData(data);
    };

    const getDataToApi = () => {
      store.getData();
    };

    return {
      personality,
      addUserInfo,
      routeTo,
      postDataToApi,
      getDataToApi,
      getDataAll: computed(() => store.getDataAll),
    };
  }
});
</script> -->
