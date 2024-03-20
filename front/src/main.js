import { createApp } from 'vue'
import App from './App.vue'
import router from './router'
import store from './store'
import './index.css'
import VueSmoothScroll from 'vue3-smooth-scroll'
import i18n from './i18n'

createApp(App).use(store).use(router).use(i18n).use(VueSmoothScroll).mount('#app')
