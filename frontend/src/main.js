import { createApp } from 'vue'
import App from './App.vue'
import router from './router'

import 'bootstrap/dist/css/bootstrap.min.css';
import 'bootstrap-vue-next/dist/bootstrap-vue-next.css';
import { BootstrapVueNextResolver } from 'bootstrap-vue-next';


const app = createApp(App)

app.use(router)
app.use(BootstrapVueNextResolver)
app.mount('#app')
