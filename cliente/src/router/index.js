import Vue from "vue";
import VueRouter from "vue-router";
import Principal from "../views/Principal";
import IngresarGrafo from "../views/IngresarGrafo";
import MatrizCaminos from "../views/MatrizCaminos";
import Dijkstra from "../views/Dijkstra";
import HamiltonianoEuleriano from "../views/HamiltonianoEuleriano";
import FlujoMaximo from "../views/FlujoMaximo";
import ArbolGenerador from "../views/ArbolGenerador";

Vue.use(VueRouter);

const routes = [{
        path: "/",
        name: "principal",
        component: Principal
    },
    {
        path: "/ingresar-grafo",
        name: "ingresar-grafo",
        component: IngresarGrafo
    },
    {
        path: "/matriz-de-caminos",
        name: "matriz-de-caminos",
        component: MatrizCaminos
    },
    {
        path: "/camino-mas-corto",
        name: "camino-mas-corto",
        component: Dijkstra
    },
    {
        path: "/hamiltoniano-o-euleriano",
        name: "hamiltoniano-o-euleriano",
        component: HamiltonianoEuleriano
    },
    {
        path: "/flujo-maximo",
        name: "flujo-maximo",
        component: FlujoMaximo
    },
    {
        path: "/arbol-generador-minimo",
        name: "arbol-generador-minimo",
        component: ArbolGenerador
    },
];

const router = new VueRouter({
    mode: "history",
    base: process.env.VUE_APP_BASE_URL,
    routes
});

export default router;