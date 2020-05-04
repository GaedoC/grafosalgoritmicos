<template>
  <div class="is-full-h" style="padding: 20px;">
    <div class="columns is-marginless is-paddingless is-full-h">
      <div class="column is-6">
        <h1 class="title is-marginless">Camino más corto</h1>
        <span class="subtitle">Algoritmo de Dijkstra</span>
        <div v-if="respuesta">
          <p>
            {{
              this.objetoRespuesta.ruta.length != 0
                ? `La duración del camino es de ${this.objetoRespuesta.pesoTotal}`
                : "La duración del camino es de ∞"
            }}
          </p>
          <p>
            {{
              this.objetoRespuesta.ruta.length != 0
                ? `La ruta fue ${this.objetoRespuesta.ruta.join(" ➜ ")}`
                : "No hay una camino entre los puntos específicados."
            }}
          </p>
        </div>
        <b-field grouped style="margin: 0; margin-top: 20px;">
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

        <b-button
          type="is-primary"
          outlined
          rounded
          expanded
          :loading="cargando"
          @click="dijkstra"
          >Calcular</b-button
        >
      </div>
      <div class="column is-6" style="border-left: 2px solid #f5f5f5; ">
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
  name: "Dijkstra",
  components: {
    Grafo,
  },
  data: () => ({
    cargando: false,
    respuesta: false,
    objetoRespuesta: null,
    origen: null,
    destino: null,
    nodos: [],
  }),
  mounted() {
    this.respuesta = false;
    this.objetoRespuesta = null;
    var nodosStore = this.$store.state.nodos;
    var nodosActuales = [];
    for (let index = 0; index < nodosStore.length; index++) {
      const element = nodosStore[index];
      nodosActuales.push(element.etiqueta);
    }
    this.nodos = nodosActuales;
  },
  methods: {
    dijkstra() {
      this.cargando = true;
      var data = {
        grafo: this.$store.getters.grafo,
        inicio: this.origen,
        final: this.destino,
      };
      axios({
        method: "post",
        url: this.$apiUrl + "/dijkstra",
        data: data,
      })
        .then((r) => {
          this.objetoRespuesta = r.data;
          this.respuesta = true;
          this.cargando = false;
        })
        .catch((e) => {
          this.cargando = false;
        });
    },
  },
};
</script>
