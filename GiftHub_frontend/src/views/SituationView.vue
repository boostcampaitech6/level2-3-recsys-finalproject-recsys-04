<template>
  <section class="bg-gray-50 text-center">
    <div class="container mx-auto flex px-5 py-10 md:flex-row flex-col items-center">
      <div class="mx-auto max-w-xl">
        <h1 class="text-3xl font-extrabold sm:text-5xl">선물을 주는 상황</h1>
        <div class="flex flex-wrap justify-center gap-4 items-center text-center">
          <table class="mx-auto mt-5 font-extrabold">
            <tr>
                <td height=100 width=100><button @click="addUserInfo('생일선물')"><img src="@/assets/생일선물.png">생일</button></td>
                <td height=100 width=100><button @click="addUserInfo('집들이선물')"><img src="@/assets/집들이선물.png">집들이</button></td>
                <td height=100 width=100><button @click="addUserInfo('새차선물')"><img src="@/assets/새차선물.png">새차</button></td>
            </tr>
            <tr>
                <td height=100 width=100><button @click="addUserInfo('퇴직선물')"><img src="@/assets/퇴직선물.png">퇴직</button></td>
                <td height=100 width=100><button @click="addUserInfo('합격기원선물')"><img src="@/assets/합격기원선물.png">합격기원</button></td>
                <td height=100 width=100><button @click="addUserInfo('개업선물')"><img src="@/assets/개업선물.png">개업</button></td>
            </tr>
            <tr>
                <td height=100 width=100><button @click="addUserInfo('취업선물')"><img src="@/assets/취업선물.png">취업</button></td>
                <td height=100 width=100><button @click="addUserInfo('결혼기념일선물')"><img src="@/assets/결혼기념일선물.png">결혼기념일</button></td>
                <td height=100 width=100><button @click="addUserInfo('출산선물')"><img src="@/assets/출산선물.png">출산</button></td>
            </tr>
          </table>
          <div class="mt-4 ml-2 mr-0 font-extrabold sm:text-xl/relaxed">
            <p>{{ category_1 }}</p>
            <h1 class="font-extrabold sm:text-xl/relaxed" v-if="category_1==''"><br>"선택해주세요."</h1>
            <button v-if="category_1!==''" @click="routeTo('/inference'), postDataToApi()" class="rounded-md px-3.5 py-2.5 text-sm font-semibold text-white bg-indigo-500 shadow-sm hover:bg-indigo-600 focus-visible:outline focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-white">선물 추천 바로가기</button>
          </div>
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
            <a class="hidden md:flex w-10 h-10 mx-1 justify-center items-center rounded-full border border-gray-200 bg-white dark:bg-gray-700 text-black dark:text-white hover:border-gray-300 dark:hover:border-gray-600"
                href="/price" title="Page 4">
                4
            </a>
            <a class="hover:border-gray-300 dark:hover:border-gray-600 hidden md:flex w-10 h-10 mx-1 justify-center items-center rounded-full border border-black dark:border-white dark:bg-black dark:text-white pointer-events-none"
                href="/situation" title="Page 5">
                5
            </a>
          </nav>
      </div>
  </section>
</template>
<script>
import { computed, defineComponent, ref } from 'vue';
import { userInfoStore } from '../store/index';

export default defineComponent({
  setup() {
    const store = userInfoStore();
    const category_1 = ref('');

    const addUserInfo = (e) => {
      store.addUserInfo({ key: 'category_1', value: e });
      category_1.value = e;
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
    return {
      category_1,
      addUserInfo,
      routeTo,
      postDataToApi,
      getDataAll: computed(() => store.getDataAll),
    };
  }
});
</script>



