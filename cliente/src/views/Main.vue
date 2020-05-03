<template>
  <div class="is-flex" style="width: 100%;">
    <div class="card" style="width: 100%; height: calc(100vh - 80px); border-radius: 20px;">
      <div class="is-full-h" style="padding: 20px;">
        <div class="columns is-marginless is-paddingless is-full-h">
          <div class="column is-6" style="overflow-y: scroll; padding-right: 20px">
            <div v-if="!vista">
              <div class="buttons are-medium">
              <button class="button is-fullwidth is-rounded is-primary is-outlined" @click="()=>{vista = 1}">Ingresar Grafo</button>
              <button class="button is-fullwidth is-rounded is-primary is-outlined">Matriz de caminos</button>
              <button class="button is-fullwidth is-rounded is-primary is-outlined">Camino más corto</button>
              <button class="button is-fullwidth is-rounded is-primary is-outlined">Hamiltoniano o Euleriano</button>
              <button class="button is-fullwidth is-rounded is-primary is-outlined">Flujo máximo</button>
              <button class="button is-fullwidth is-rounded is-primary is-outlined">Árbol generador mínimo</button>
              </div>
            </div>
            <div v-else-if="vista == 1">
            <stepper-data :volver="()=>{vista = 0}" :nodos="nodos"/>
            </div>
          </div>
          <div class="column is-6">
            <div v-if="!vista">
              <div class="container" style="height: 100%; padding: 40px;">
              <p class="title">Universidad Tecnológica Metropolitana</p>
              <p class="subtitle">/Grafos y Lenguajes Formales</p>
              <p>Integrantes: </p>
                  <li>Integrante 1</li>
                  <li>Integrante 2</li>
                  <li>Integrante 3</li>
                  <li>Integrante 4</li>
                  <li>Integrante 5</li>
              </div>
            </div>
            <div v-else-if="vista == 1">
            <cytoscape
              ref="cy"
              :config="config"
              :afterCreated="afterCreated"
              style="border-left: 2px solid #f5f5f5; height: 100%;"
            >
              <cy-element v-for="def in elementos" :key="`${def.data.id}`" sync :definition="def" />
            </cytoscape>
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import StepperData from "../components/StepperData.vue";

export default {
  name: "Main",
  components: {
    StepperData
  },
  data: () => ({
    indiceMaximo: 1,
    vista: 0,
    nodos: ["A"],
    cy: null,
    config: {
      style: [
        {
          selector: "node",
          style: {
            "background-color": "#7958d5",
            label: "data(id)"
          }
        }
      ],
      layout: { name: "grid", rows: 3 }
    }
  }),
  watch: {
    elementos() {
      this.$nextTick(() => {
        const cy = this.$refs.cy.instance;
        this.afterCreated(cy);
      });
    }
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
              y: 1
            },
            group: "nodes"
          });
        }
      }
      return nodos;
    }
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
    }
  }
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
