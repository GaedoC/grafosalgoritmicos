<template>
  <div class="is-full-h" style="padding: 20px;">
    <b-field grouped v-for="(etiqueta, i) in nodos" :key="i">
      <b-field expanded>
        <b-input v-model="nodos[i]" rounded></b-input>
      </b-field>
      <b-tooltip v-if="nodos.length > 1" label="Eliminar" class="is-danger" position="is-left">
        <a @click="eliminarNodo(i)" style="margin-top: 5px;">
          <b-icon pack="fa" class="is-danger" style="margin-top: 5px;" icon="minus-circle"></b-icon>
        </a>
      </b-tooltip>
      <div v-else style="margin-top: 5px;">
        <b-icon pack="fa" icon="minus-circle" style="color: grey;"></b-icon>
      </div>
    </b-field>
    <b-button
      class="is-marginless"
      type="is-primary"
      style=" margin: 12px;"
      outlined
      rounded
      expanded
      @click="agregarNodo"
      icon-left="plus-circle"
    >Agregar nodo</b-button>
  </div>
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
  name: "NodosInput",
  props: ["nodos"],
  data: () => ({
    indiceMaximo: 1,
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
