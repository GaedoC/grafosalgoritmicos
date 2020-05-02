import Vue from 'vue';
import App from './App.vue';
import Buefy from 'buefy';
import VueCytoscape from 'vue-cytoscape';
import 'buefy/dist/buefy.css';

Vue.config.productionTip = false;

Vue.use(Buefy);
Vue.use(VueCytoscape);

new Vue({
  render: h => h(App),
}).$mount('#app');