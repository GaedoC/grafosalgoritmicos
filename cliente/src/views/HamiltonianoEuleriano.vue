<template>
  <div class="is-full-h" style="padding: 20px;">
    <div class="columns is-marginless is-paddingless is-full-h">
      <div class="column is-6" style="overflow-y: scroll; padding-right: 20px">
        <p class="title">¿Grafo Euleriano o Hamiltoniano?</p>
        <b-button
          type="is-primary"
          outlined
          rounded
          expanded
          v-if="!calculado"
          class="button"
          >Determinar</b-button
        >
        <div v-else>
          <b-button type="is-primary" outlined rounded expanded :disabled="true"
            >Calcular</b-button
          >
          <p>La matriz de caminos es conexa</p>
        </div>
      </div>
      <div class="column is-6">
        <grafo
          :nodos="$store.state.nodos"
          :origenes="$store.state.origenes"
          :destinos="$store.state.destinos"
          :pesos="$store.state.pesos"
        />
      </div>
    </div>
  </div>
</template>

<script>
import axios from "axios";
import Grafo from "../components/Grafo.vue";

export default {
  name: "MatrizCaminos",
  components: {
    Grafo,
  },
  data: () => ({
    indiceMaximo: 1,
    calculado: false,
    nodos: [],
    cy: null,
    config: {
      style: [
        {
          selector: "node",
          style: {
            "background-color": "#7958d5",
            label: "data(id)",
          },
        },
      ],
      layout: { name: "grid", rows: 3 },
    },
  }),
  watch: {
    elementos() {
      this.$nextTick(() => {
        const cy = this.$refs.cy.instance;
        this.afterCreated(cy);
      });
    },
  },
  computed: {
    elementos() {
      var nodos = [];
      for (const etiqueta of this.nodos) {
        if (etiqueta && etiqueta != "") {
          nodos.push({
            data: { id: etiqueta },
            position: {
              x: 1,
              y: 1,
            },
            group: "nodes",
          });
        }
      }
      return nodos;
    },
  },
  methods: {
    agregarNodo() {
      this.indiceMaximo++;
      var valorAsciiA = 65;
      var caracter = String.fromCharCode(valorAsciiA + this.indiceMaximo);
      this.nodos.push(caracter);
    },
    eliminarNodo(i) {
      this.nodos.splice(i, 1);
    },
    async afterCreated(cy) {
      await cy;
      cy.layout(this.config.layout).run();
    },
    obtenerMatriz() {
      axios({
        method: post,
        url: this.$apiUrl + "/matriz",
        data: this.grafo,
      })
        .then((r) => {
          console.log("Respuesta", r.data);
        })
        .catch((e) => {
          console.log(e);
        });
    },
  },
};
</script>

<style>
#cytoscape-div {
  min-height: 100px;
  height: 100%;
}

#cytoscape-div,
#cytoscape-div > div,
#cytoscape-div > div > canvas {
  min-height: 100px !important;
  height: 100% !important;
}
</style>
