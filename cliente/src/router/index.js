import Vue from "vue";
import VueRouter from "vue-router";
import Principal from "../views/Principal";
import Primera from "../views/Primera";
import Segunda from "../views/Segunda";
import Tercera from "../views/Tercera";
import Cuarta from "../views/Cuarta";
import Quinta from "../views/Quinta";
import Sexta from "../views/Sexta";
import store from "../store";

Vue.use(VueRouter);

const routes = [{
        path: "/",
        name: "principal",
        component: Principal
    },
    {
        path: "/ingresar-grafo",
        name: "ingresar-grafo",
        component: Primera
    },
    {
        path: "/matriz-de-caminos",
        name: "matriz-de-caminos",
        component: Segunda
    },
    {
        path: "/camino-mas-corto",
        name: "camino-mas-corto",
        component: Tercera
    },
    {
        path: "/hamiltoniano-o-euleriano",
        name: "hamiltoniano-o-euleriano",
        component: Cuarta
    },
    {
        path: "/flujo-maximo",
        name: "flujo-maximo",
        component: Quinta
    },
    {
        path: "/arbol-generador-minimo",
        name: "arbol-generador-minimo",
        component: Sexta
    },
];

const router = new VueRouter({
    mode: "history",
    base: process.env.VUE_APP_BASE_URL,
    routes
});

export default router;