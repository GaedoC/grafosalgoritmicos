import Vue from "vue";
import App from "./App.vue";
import Buefy from "buefy";
import VueKatex from "vue-katex";
import VueCytoscape from "vue-cytoscape";
import router from "./router";
import VueSidebarMenu from 'vue-sidebar-menu';

import "buefy/dist/buefy.css";
import "katex/dist/katex.min.css";
import 'vue-sidebar-menu/dist/vue-sidebar-menu.css'

Vue.config.productionTip = false;

Vue.use(Buefy);
Vue.use(VueCytoscape);
Vue.use(VueSidebarMenu);
Vue.use(VueKatex, {
  globalOptions: {},
});
Vue.prototype.$apiUrl = "http://localhost:5151";

new Vue({
  router,
  render: (h) => h(App),
}).$mount("#app");
