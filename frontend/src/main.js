import { createApp } from 'vue';
import App from './App.vue';
import router from './router';

createApp(App)
    .use(router)  // Usa il router con Vue 3
    .mount('#app');
