<template>
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
</template>

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

<script>
export default {
  name: "Grafo",
  props: ["nodos", "origenes", "destinos", "pesos"],
  data: () => ({
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
  },
  methods: {
    async afterCreated(cy) {
      await cy;
      cy.layout(this.config.layout).run();
    },
  },
};
</script>
