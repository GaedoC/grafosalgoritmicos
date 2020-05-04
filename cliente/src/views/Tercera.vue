<template>
  <div class="is-flex" style="width: 100%;">
    <div class="card" style="width: 100%; height: calc(100vh - 80px); border-radius: 10px;">
      <div class="is-full-h" style="padding: 20px;">
        <div class="columns is-marginless is-paddingless is-full-h">
          <div class="column is-6" style="overflow-y: scroll; padding-right: 20px">
            <p class="title">Camino más corto</p>
            <div class="column" v-if="!calculado">
              <b-field grouped class="is-marginless">
                <b-field expanded>
                  <b-autocomplete
                    rounded
                    v-model="origen"
                    :data="nodos"
                    keep-first
                    open-on-focus
                    field="etiqueta"
                    placeholder="Nodo de origen"
                    clearable
                  >
                    <template slot="empty">Sin resultados</template>
                  </b-autocomplete>
                </b-field>
                <b-field expanded>
                  <b-autocomplete
                    rounded
                    v-model="destino"
                    :data="nodos"
                    keep-first
                    open-on-focus
                    field="etiqueta"
                    placeholder="Nodo de destino"
                    clearable
                  >
                    <template slot="empty">Sin resultados</template>
                  </b-autocomplete>
                </b-field>
              </b-field>
              <b-button type="is-primary" outlined rounded expanded>Calcular</b-button>
            </div>
            <div v-else>
              <b-button type="is-primary" outlined rounded expanded :disabled="true">Calcular</b-button>
              <p>El camino más corto es</p>
            </div>
          </div>
          <div class="column is-6">
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
</template>

<script>
export default {
  name: "Tercera",
  components: {},
  data: () => ({
    indiceMaximo: 1,
    calculado: false,
    origen: null,
    destino: null,
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
    },
    dijkstra() {
      var data = {
        grafo: this.grafo,
        inicio: this.origen,
        final: this.destino
      };
      axios({
        method: post,
        url: this.$apiUrl + "/dijkstra",
        data: data
      })
        .then(r => {
          console.log("Respuesta", r.data);
        })
        .catch(e => {
          console.log(e);
        });
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