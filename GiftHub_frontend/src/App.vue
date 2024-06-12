<template>
  <Header />
  <router-view />
  <!-- <Footer /> -->
</template>

<script>
import Header from './views/layout/HeaderView.vue';
import Footer from './views/layout/FooterView.vue';

export default {
  name: 'App',
  components: {
    Header,
    Footer
  }
}
</script>