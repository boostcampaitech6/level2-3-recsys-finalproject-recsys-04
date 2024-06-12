<!--숫자 이외의 문자가 입력되는 버그 해결해야함-->
<template>
  <section class="bg-gray-50 text-center">
    
    <div class="mx-auto max-w-screen-xl px-4 py-32 lg:flex lg:h-screen lg:items-center">
      <div class="mx-auto max-w-xl">
        <h1 class="text-3xl font-extrabold sm:text-5xl">선물 받을 사람의 나이는?</h1>
        <input class="mb-5 mt-5 text-center rounded-lg border-transparent flex-1 appearance-none border border-gray-300 w-full py-2 px-4 bg-white text-gray-700 placeholder-gray-400 shadow-sm text-base focus:outline-none focus:ring-2 focus:ring-purple-600 focus:border-transparent" type="number" @keyup.enter="addUserInfo(input)" v-model="input" maxlength="2" placeholder="여기에 입력해주세요" min="1" max="99"/>
        <button @click="addUserInfo(input)" class="rounded-md bg-white px-3.5 py-2.5 text-sm font-semibold text-gray-900 shadow-sm hover:bg-gray-100 focus-visible:outline focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-white">제출</button>
        <div class="mt-4 sm:text-xl/relaxed">
          {{age}}살
        </div>
          <div class="absolute py-10 inset-x-0 bottom-0 h-40 ...">
            <nav class="flex flex-row flex-nowrap justify-between md:justify-center items-center" aria-label="Pagination">
              <!-- Previous Page Button -->
              <a class="flex w-10 h-10 mr-1 justify-center items-center rounded-full border border-gray-200 bg-white dark:bg-gray-800 text-black dark:text-white hover:border-gray-300 dark:hover:border-gray-600"
              href="/gender" title="Previous Page">
                  <span class="sr-only">Previous Page</span>
                  <svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke-width="1.5"
                      stroke="currentColor" class="block w-5 h-5">
                      <path stroke-linecap="round" stroke-linejoin="round" d="M15.75 19.5L8.25 12l7.5-7.5" />
                  </svg>
                </a>
              <!-- Page Buttons (1 to 5) -->
              <a class="hidden md:flex w-10 h-10 mx-1 justify-center items-center rounded-full border border-gray-200 bg-white dark:bg-gray-700 text-black dark:text-white hover:border-gray-300 dark:hover:border-gray-600"
                  href="/gender" title="Page 1">
                  1
              </a>
              <a class="hover:border-gray-300 dark:hover:border-gray-600 hidden md:flex w-10 h-10 mx-1 justify-center items-center rounded-full border border-black dark:border-white dark:bg-black dark:text-white pointer-events-none"
                  href="/age" aria-current="page" title="Page 2">
                  2
              </a>
              <a class="hidden md:flex w-10 h-10 mx-1 justify-center items-center rounded-full border border-gray-200 bg-white dark:bg-gray-700 text-black dark:text-white hover:border-gray-300 dark:hover:border-gray-600"
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
              href="/color" title="Next Page">
                  <span class="sr-only">Next Page</span>
                  <svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke-width="1.5"
                      stroke="currentColor" class="block w-5 h-5">
                      <path stroke-linecap="round" stroke-linejoin="round" d="M8.25 4.5l7.5 7.5-7.5 7.5" />
                  </svg>
              </a>
            </nav>
        </div>
      </div>
    </div>
  </section>
</template>

<script>
import { watch ,computed, defineComponent, ref } from 'vue';
import { userInfoStore } from '../store/index';

export default defineComponent({
  setup() {
    const store = userInfoStore();
    const age = ref(0); // 성별을 저장할 ref
    const input = ref(0);

    const addUserInfo = (e) => {
      store.addUserInfo({ key: 'age', value: e });
      age.value = e; // age 값 갱신
    };

    const routeTo = (path) => {
      // router를 import하여 사용
      store.routeTo(path);
    };
  
    return {
      age,
      addUserInfo,
      routeTo,
      getDataAll: computed(() => store.getDataAll),
    };
  }
});
</script>