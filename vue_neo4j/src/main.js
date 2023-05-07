import Vue from 'vue'
import App from './App.vue'
import router from './router'
import store from './store'
import ElementUI from 'element-ui';
import 'element-ui/lib/theme-chalk/index.css';
// import * as echarts from 'echarts'
import request from "@/utils/request";
// main.js中引入样式
import 'video.js/dist/video-js.min.css'





Vue.config.productionTip = false
Vue.use(ElementUI);
// Vue.prototype.$echarts = echarts
Vue.prototype.request=request


new Vue({
  router,
  store,
  render: h => h(App)
}).$mount('#app')


