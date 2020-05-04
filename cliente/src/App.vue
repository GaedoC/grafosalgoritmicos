<template>
  <div
    class="is-flex"
    style="justify-content: center;
    align-items: center;
    height: 100%; padding: 40px;"
  >
    <div>
      <sidebar-menu :menu="menu" :collapsed="true" :width="`260px`"/>
      <router-view />
    </div>
  </div>
</template>

<script>
import Principal from "./views/Principal.vue";

export default {
  name: "App",
  components: {
    Principal,
  },
  data() {
    return {
      menu: [
        {
          href: "/",
          title: "Presentación",
          icon: "checkbox-blank-circle-outlined"
        },
        {
          href: "/ingresar-grafo",
          title: "Ingresar Grafo",
          icon: "checkbox-blank-circle-outlined"
        },
        {
          href: "/matriz-de-caminos",
          title: "Matriz de Caminos",
          icon: "checkbox-blank-circle-outlined"
        },
        {
          href: "/camino-mas-corto",
          title: "Camino más corto",
          icon: "checkbox-blank-circle-outlined"
        },
        {
          href: "/hamiltoniano-o-euleriano",
          title: "¿Hamiltoniano o Euleriano?",
          icon: "checkbox-blank-circle-outlined"
        },
        {
          href: "/flujo-maximo",
          title: "Flujo máximo",
          icon: "checkbox-blank-circle-outlined"
        },
        {
          href: "/arbol-generador-minimo",
          title: "Árbol generador mínimo",
          icon: "checkbox-blank-circle-outlined"
        },
      ]
    };
  }
};
</script>

<style>
html,
body {
  height: 100%;
  min-height: 100%;
}

body {
  background-color: #7958d5;
}

.is-full-h {
  height: 100% !important;
}
</style>
