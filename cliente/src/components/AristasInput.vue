<template>
  <div class="is-full-h" style="padding: 20px;">
    <b-field grouped v-for="(origen, i) in origenes" :key="i">
      <b-field expanded>
        <b-select placeholder="Nodo de origen" v-model="origenes[i]">
          <option v-for="nodo in nodos" :value="nodo" :key="nodo">{{ nodo }}</option>
        </b-select>
      </b-field>
      <b-field expanded>
        <b-select placeholder="Nodo de destino" v-model="destinos[i]">
          <option v-for="nodo in nodos" :value="nodo" :key="nodo">{{ nodo }}</option>
        </b-select>
      </b-field>
      <b-field>
        <b-numberinput
          controls-position="compact"
          controls-rounded
          expanded
          style="width: 150px"
          min="0"
          v-model="pesos[i]"
        ></b-numberinput>
      </b-field>

      <b-tooltip
        v-if="origenes.length > 1"
        label="Eliminar"
        class="is-danger"
        position="is-left"
        style="margin-top: -25px;"
      >
        <a @click="eliminarArista(i)" style="margin-top: 30px;">
          <b-icon pack="fa" class="is-danger" icon="minus-circle"></b-icon>
        </a>
      </b-tooltip>
      <div v-else style="margin-top: 5px;">
        <b-icon pack="fa" icon="minus-circle" style="color: grey;"></b-icon>
      </div>
    </b-field>
    <div class="is-marginless is-paddingless">
      <b-button
        type="is-primary"
        style=" margin: 12px;"
        outlined
        rounded
        expanded
        @click="agregarArista"
        icon-left="plus-circle"
      >Agregar arista</b-button>
    </div>
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
  name: "AristasInput",
  props: ["nodos"],
  data: () => ({
    origenes: [null],
    destinos: [null],
    pesos: [0],
    config: {
      style: [
        {
          selector: "node",
          style: {
            "background-color": "#7958d5",
            label: "data(id)"
          }
        },
        {
          selector: "edge",
          style: {
            width: 3,
            "curve-style": "bezier",
            "line-color": "#ccc",
            "target-arrow-color": "#ccc",
            "target-arrow-shape": "triangle"
          }
        }
      ],
      layout: { name: "circle", row: 1 }
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
      var elementos = [];
      for (const etiqueta of this.nodos) {
        if (etiqueta && etiqueta != "") {
          elementos.push({
            data: { id: etiqueta },
            position: {
              x: 1,
              y: 1
            },
            group: "nodes"
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
              type: "loop"
            },
            group: "edges"
          });
        }
      }
      return elementos;
    },
    grafo() {
      var aristas = [];
      for (let i = 0; i < this.origenes.length; i++) {
        const origen = this.origenes[i];
        const destino = this.destinos[i];
        const peso = this.pesos[i];

        aristas.push({
          inicio: origen,
          final: destino,
          peso: peso
        });
      }
      return {
        grafo: aristas
      };
    }
  },
  methods: {
    agregarArista() {
      this.origenes.push(null);
      this.destinos.push(null);
      this.pesos.push(0);
    },
    eliminarArista(i) {
      this.origenes.splice(i, 1);
      this.destinos.splice(i, 1);
      this.pesos.splice(i, 1);
    },
    validarNodo(valor) {
      if (valor != null) {
        if (this.nodos.indexOf(valor) < 0) {
          return "Debe seleccionar un nodo válido";
        }
      }
      return null;
    },
    getNodosFiltrados(valor) {
      if (valor != null) {
        return this.nodos.filter(n => {
          n.toString()
            .toLowerCase()
            .includes(valor.toString().toLowerCase);
        });
      }
      return this.nodos;
    },
    async afterCreated(cy) {
      await cy;
      cy.layout(this.config.layout).run();
    }
  }
};
</script>
