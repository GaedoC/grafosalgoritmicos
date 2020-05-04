<template>
  <div class="is-full-h" style="padding: 20px;">
    <div class="columns is-marginless is-paddingless is-full-h">
      <div
        class="column is-6 is-full-h"
        style="display: flex; flex-direction: column; justify-content: space-between;"
      >
        <h1 class="title">Matriz de camino</h1>
        <matriz v-if="matriz != null" :vertices="vertices" :matriz="matriz" />
        <b-field expanded position="is-centered">
          <b-numberinput
            controls-position="compact"
            controls-rounded
            style="max-width: 200px"
            min="0"
            v-model="peso"
          ></b-numberinput>
        </b-field>
        <b-button
          type="is-primary"
          outlined
          rounded
          expanded
          :loading="cargando"
          @click="obtenerMatriz"
          class="button"
          >Calcular</b-button
        >
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
    peso: 0,
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
      this.cargando = true;
      axios({
        method: "post",
        url: this.$apiUrl + "/matriz",
        data: {
          largo: this.peso,
          grafo: this.$store.getters.grafo,
        },
      })
        .then((r) => {
          this.cargando = false;
          this.matriz = r.data.matriz;
          this.vertices = r.data.vertices;
          this.esConexo = r.data.esConexo;
        })
        .catch((e) => {
          console.log(e);
          this.cargando = false;
        });
    },
  },
};
</script>
