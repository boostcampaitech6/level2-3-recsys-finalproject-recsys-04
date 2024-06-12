import { createApp } from 'vue'
import App from './App.vue'
import router from './router'
import './assets/css/index.css' // tailwind css
import { createPinia } from 'pinia';
import piniaPluginPersistedstate from 'pinia-plugin-persistedstate'

const app = createApp(App);
app.use(router);
app.use(createPinia().use(piniaPluginPersistedstate));
app.mount('#app');
