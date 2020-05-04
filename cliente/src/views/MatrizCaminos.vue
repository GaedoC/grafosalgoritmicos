<template>
  <div class="is-full-h" style="padding: 20px;">
    <div class="columns is-marginless is-paddingless is-full-h">
      <div
        class="column is-6 is-full-h"
        style="display: flex; flex-direction: column; justify-content: space-between;"
      >
        <h1 class="title">Matriz de camino</h1>
        <matriz v-if="matriz != null" :vertices="vertices" :matriz="matriz" />
        <b-button
          type="is-primary"
          outlined
          rounded
          expanded
          @click="obtenerMatriz"
          class="button"
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
import Matriz from "../components/Matriz.vue";

export default {
  name: "MatrizCaminos",
  components: {
    Grafo,
    Matriz,
  },
  data: () => ({
    cargando: false,
    matriz: null,
    vertices: [],
    esConexo: null,
  }),
  methods: {
    matrizToKaTexMatrix(matriz) {
      var exp = String.raw`\begin{pmatrix}`;
      var esPrimeraFila = true;
      for (const fila of matriz) {
        var esPrimerElemento = true;
        if (!esPrimeraFila) {
          exp += String.raw`\\`;
        }
        for (const elemento of fila) {
          if (!esPrimerElemento) {
            exp += String.raw` & `;
          }
          exp += elemento.toString();
          esPrimerElemento = false;
        }
        esPrimeraFila = false;
      }
      exp += String.raw`\end{pmatrix}`;
      return exp;
    },
    obtenerMatriz() {
      axios({
        method: "post",
        url: this.$apiUrl + "/matriz",
        data: {
          largo: 1,
          grafo: this.$store.getters.grafo,
        },
      })
        .then((r) => {
          this.matriz = r.data.matriz;
          this.vertices = r.data.vertices;
          this.esConexo = r.data.esConexo;
          console.log(this.matriz);
        })
        .catch((e) => {
          console.log(e);
        });
    },
  },
};
</script>
