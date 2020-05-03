import Vue from "vue";
import App from "./App.vue";
import Buefy from "buefy";
import VueKatex from 'vue-katex';
import VueCytoscape from "vue-cytoscape";

import "buefy/dist/buefy.css";
import 'katex/dist/katex.min.css';

Vue.config.productionTip = false;

Vue.use(Buefy);
Vue.use(VueCytoscape);
Vue.use(VueKatex, {
  globalOptions: {}
});

new Vue({
  render: (h) => h(App),
}).$mount("#app");