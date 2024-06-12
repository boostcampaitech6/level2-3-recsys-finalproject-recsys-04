<template>
  <section class="text-gray-600 body-font">
    <div class="container mx-auto flex px-5 py-14 md:flex-row flex-col items-center">
      <div class="lg:flex-grow md:w-1/2 lg:pr-24 md:pr-16 flex flex-col md:items-start md:text-left mb-16 md:mb-0 items-center text-center">
        <h1 class="title-font sm:text-4xl text-3xl mb-4 font-medium text-gray-900">특별한 날
          <br class="hidden lg:inline-block">더 특별해지고 싶은 당신을 위한 추천
          <br class="hidden lg:inline-block">GiftHub 선물 추천
        </h1>
        <p class="mt-3 mb-8 leading-relaxed">특별한 날, 당신을 위한 더 특별한 순간을 만들어줄 선물 아이디어! 
          <br class="hidden lg:inline-block">이번 특별한 날에는 평범한 것과는 차별화된 감동을 선사해보세요. 
          <br class="hidden lg:inline-block">GiftHub이 준비한 선물 추천으로 당신의 특별한 날을 더욱 의미있게 만들어보세요.
        </p>
        <div class="flex justify-center">
          <button @click="routeTo('/gender')" class="w-64 rounded-md text-white bg-indigo-500 px-3.5 py-2.5 text-sm font-semibold text-gray-900 shadow-sm hover:bg-indigo-600 focus-visible:outline focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-white">선물 추천 바로가기</button>
        </div>
      </div>
      <div class="lg:max-w-lg lg:w-full md:w-1/2 w-5/6">
        <img class="object-cover object-center rounded" alt="hero" src="@/assets/GiftHub_logo_2.png">
      </div>
    </div>
  </section>
</template>
<script>
export default {
    methods: {
      routeTo(path) {
        this.$router.push(path);
      },
    }
}
</script>
<style>
.bg-white {
  width: 100%;
  height: 100%;
}
</style>
