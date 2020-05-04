<template>
  <div class="is-flex" style="width: 100%;">
    <div
      class="card"
      style="width: 100%; height: calc(100vh - 80px); border-radius: 10px;"
    >
      <div class="is-full-h" style="padding: 20px;">
        <div class="columns is-marginless is-paddingless is-full-h">
          <div
            class="column is-6 is-full-h"
            style="display: flex; flex-direction: column; justify-content: space-between;"
          >
            <h1 class="title">Matriz de camino</h1>
            <katex-element
              :expression="
                matrizToKaTexMatrix([
                  [1, 2, 3, 4, 5],
                  [3, 4, 5, 6, 7],
                  [1, 2, 3, 4, 5],
                  [3, 4, 5, 6, 7],
                  [3, 4, 5, 6, 7],
                ])
              "
            />
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
    cargando: false,
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
        data: this.$store.getters.grafo,
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
