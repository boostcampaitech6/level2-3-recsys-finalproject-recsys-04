<template>
  <section class="bg-gray-50 text-center">
    <div class="mx-auto max-w-screen-xl px-4 py-32 lg:flex lg:h-screen lg:items-center">
      <div class="mx-auto max-w-xl ">
        <h1 class="text-3xl font-extrabold sm:text-5xl">선물 받을 사람의 성별은?</h1>
        <h1 class="mt-4 font-extrabold sm:text-xl/relaxed" v-show="sex=='M'"><br>"남자분께 선물하시는군요."</h1>
        <h1 class="mt-4 font-extrabold sm:text-xl/relaxed" v-show="sex=='F'"><br>"여자분께 선물하시는군요."</h1>
        <h1 class="mt-4 font-extrabold sm:text-xl/relaxed" v-show="sex==''"><br>"선택해주세요."</h1>
        <div class="mt-8 flex flex-wrap justify-center gap-4">
          <button class="block w-full rounded bg-red-600 px-12 py-3 text-sm font-extrabold text-white shadow hover:bg-red-700 focus:outline-none focus:ring active:bg-red-500 sm:w-auto" @click="addUserInfo('M')">남</button>
          <button class="block w-full rounded px-12 py-3 text-sm font-extrabold text-red-600 shadow hover:text-red-700 focus:outline-none focus:ring active:text-red-500 sm:w-auto" @click="addUserInfo('F')">여</button><br><br>
        </div>
      </div>
      <div class="absolute py-10 inset-x-0 bottom-0 h-40 ...">
          <nav class="flex flex-row flex-nowrap justify-between md:justify-center items-center" aria-label="Pagination">
            <!-- Previous Page Button -->
            <a class="flex w-10 h-10 mr-1 justify-center items-center rounded-full border border-gray-200 bg-white dark:bg-gray-800 text-black dark:text-white hover:border-gray-300 dark:hover:border-gray-600"
            href="/" title="Previous Page">
                <span class="sr-only">Previous Page</span>
                <svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke-width="1.5"
                    stroke="currentColor" class="block w-5 h-5">
                    <path stroke-linecap="round" stroke-linejoin="round" d="M15.75 19.5L8.25 12l7.5-7.5" />
                </svg>
              </a>
            <!-- Page Buttons (1 to 5) -->
            <button class="hover:border-gray-300 dark:hover:border-gray-600 hidden md:flex w-10 h-10 mx-1 justify-center items-center rounded-full border border-black dark:border-white dark:bg-black dark:text-white pointer-events-none"
                href="/gender" aria-current="page" title="Page 1">
                1
            </button>
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
            <a class="hidden md:flex w-10 h-10 mx-1 justify-center items-center rounded-full border border-gray-200 bg-white dark:bg-gray-700 text-black dark:text-white hover:border-gray-300 dark:hover:border-gray-600"
                href="/situation" title="Page 5">
                5
            </a>
            <!-- Next Page Button -->
            <a class="flex w-10 h-10 ml-1 justify-center items-center rounded-full border border-gray-200 bg-white dark:bg-gray-800 text-black dark:text-white hover:border-gray-300 dark:hover:border-gray-600"
            href="/age" title="Next Page">
                <span class="sr-only">Next Page</span>
                <svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke-width="1.5"
                    stroke="currentColor" class="block w-5 h-5">
                    <path stroke-linecap="round" stroke-linejoin="round" d="M8.25 4.5l7.5 7.5-7.5 7.5" />
                </svg>
            </a>
          </nav>
      </div>
    </div>
  </section>
</template>
<script>
import { computed, defineComponent, ref } from 'vue';
import { userInfoStore } from '../store/index';

export default defineComponent({
  setup() {
    const store = userInfoStore();
    const sex = ref(''); // 성별을 저장할 ref

    const addUserInfo = (e) => {
      store.addUserInfo({ key: 'sex', value: e });
      sex.value = e; // sex 값 갱신
    };

    const routeTo = (path) => {
      // router를 import하여 사용
      store.routeTo(path);
    };

    return {
      sex,
      addUserInfo,
      routeTo,
      getDataAll: computed(() => store.getDataAll),
    };
  }
});
</script>
<!-- <script>
import { defineComponent } from 'vue';
import { userInfoStore } from '../store/index';

export default defineComponent({
setup() {
  const store = useStore(userInfoStore);
  const addUserInfo = (e) => {
    store.addUserInfo({ key: 'sex', value: e });
  };

  const routeTo = (path) => {
    router.push(path);
  };

  const sex = store.userInfo.sex; // 데이터 확인용

  return {
    addUserInfo,
    routeTo,
    sex
  };
}
});
</script> -->


<!-- <template>
    <h1>선물 받을 사람의 성별은?</h1>
    <h1><br>{{ sex }}</h1> 
    <button @click="addUserInfo('M')">남</button>
    <button @click="addUserInfo('F')">여</button><br><br>
    <button @click="routeTo('/')">prev</button>
    <button @click="routeTo('/age')">next</button>
</template>

<script>
import { mapActions } from 'vuex';

export default {
  data() {
    return {
      key: 'sex',
      value: ''
    };
  },
  methods: {
    routeTo(path) {
          this.$router.push(path);
    },
    ...mapActions(['addUserInfo']),
    addUserInfo(e) {
      // Vuex 액션을 호출하여 데이터 추가
      this.value = e
      this.addUserInfo({ key: this.key, value: this.value });
      // 입력 필드 초기화
      this.key = '';
      this.value = '';
    }
  }
};
</script> -->

<!-- // export default {
//     data() {
//       return {
//         sex: '',
//       }
//     },
//     computed: {
//       ...mapState(useStore(userInfoStore), {
//         userInfo: 'getAllList', // userInfoStore의 getter를 참조합니다.
//       }),
//     },
//     methods: {
//       ...mapActions(useStore(userInfoStore), ["addUserInfo"]),
//       routeTo(path) {
//         this.$router.push(path);
//       },
//       getData(e) {
//         this.sex = e;
//         this.addUserInfo("sex", this.sex);
//       }
//     }
// }
// </script> -->
// <!-- <script>
// import { userInfoStore } from '../store/index';
// import { useStore } from 'pinia';
// const userInfo = userInfoStore()
// const newInfo = ref('')

// function getData(e){
//   newInfo = e
//   userInfo.addUserInfo('sex',newInfo.value)
// }
// </script> -->




<!-- <template>
  <h1>선물 받을 사람의 성별은?</h1>
  <h1><br>{{ sex }}</h1> //data 확인용
  <button @click="getData('M')">남</button>
  <button @click="getData('F')">여</button><br><br>
  <button @click="routeTo('/')">prev</button>
  <button @click="routeTo('/age')">next</button>
</template>
<script>
export default {
    data(){
      return {
        sex:''
      }
    },
    methods: {
      routeTo(path) {
        this.$router.push(path);
      },
      getData(e){
        this.sex = e
      }
    }
}
</script> -->