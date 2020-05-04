<template>
  <div class="is-flex" style="width: 100%;">
    <div
      class="card"
      style="width: 100%; height: calc(100vh - 80px); border-radius: 10px;"
    >
      <div class="is-full-h" style="padding: 20px;">
        <div class="columns is-marginless is-paddingless is-full-h">
          <div class="column is-paddingless is-7">
            <stepper
              :nodos="nodos"
              :origenes="origenes"
              :destinos="destinos"
              :pesos="pesos"
              :onFinalizar="onFinalizar"
            />
          </div>
          <div class="column is-paddingless is-5">
            <cytoscape
              ref="cy"
              :config="config"
              :afterCreated="afterCreated"
              style="border-left: 2px solid #f5f5f5; height: 100%;"
            >
              <cy-element
                v-for="def in elementos"
                :key="`${def.data.id}`"
                sync
                :definition="def"
              />
            </cytoscape>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import Stepper from "../components/Stepper.vue";

export default {
  name: "Main",
  components: {
    Stepper,
  },
  data: () => ({
    nodos: [],
    origenes: [],
    destinos: [],
    pesos: [],
    config: {
      style: [
        {
          selector: "node",
          style: {
            "background-color": "#7958d5",
            label: "data(id)",
          },
        },
        {
          selector: "edge",
          style: {
            width: 3,
            "curve-style": "bezier",
            "line-color": "#ccc",
            "target-arrow-color": "#ccc",
            "target-arrow-shape": "triangle",
          },
        },
      ],
      layout: { name: "circle", row: 1 },
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
      var elementos = [];
      for (const nodo of this.nodos) {
        if (nodo && nodo.etiqueta && nodo.etiqueta != "") {
          elementos.push({
            data: { id: nodo.etiqueta },
            position: {
              x: 1,
              y: 1,
            },
            group: "nodes",
          });
        }
      }
      for (let i = 0; i < this.origenes.length; i++) {
        const origen = this.origenes[i];
        const destino = this.destinos[i];
        if (origen && destino) {
          elementos.push({
            data: {
              id: origen + destino,
              source: origen,
              target: destino,
              type: "loop",
            },
            group: "edges",
          });
        }
      }
      return elementos;
    },
    grafo() {
      var aristas = [];
      var vertices = [];

      for (const nodo of this.nodos) {
        vertices.push(nodo.etiqueta);
      }

      for (let i = 0; i < this.origenes.length; i++) {
        const origen = this.origenes[i];
        const destino = this.destinos[i];
        const peso = this.pesos[i];

        aristas.push({
          inicio: origen,
          final: destino,
          peso: peso,
        });
      }
      return {
        grafo: {
          aristas,
          vertices,
        },
      };
    },
  },
  methods: {
    async afterCreated(cy) {
      await cy;
      cy.layout(this.config.layout).run();
    },
    onFinalizar() {
      console.log(this.grafo);
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
