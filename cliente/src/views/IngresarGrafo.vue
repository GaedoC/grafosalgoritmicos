<template>
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
        <grafo
          :nodos="nodos"
          :origenes="origenes"
          :destinos="destinos"
          :pesos="pesos"
        />
      </div>
    </div>
  </div>
</template>

<script>
import Stepper from "../components/Stepper.vue";
import Grafo from "../components/Grafo.vue";

export default {
  name: "Main",
  components: {
    Stepper,
    Grafo,
  },
  data: () => ({
    nodos: [],
    origenes: [],
    destinos: [],
    pesos: [],
  }),
  mounted() {
    this.nodos = this.$store.state.nodos;
    this.origenes = this.$store.state.origenes;
    this.destinos = this.$store.state.destinos;
    this.pesos = this.$store.state.pesos;
  },
  methods: {
    onFinalizar() {
      console.log(this.nodos, this.origenes, this.destinos, this.pesos);
      this.$store.commit("crearGrafo", {
        nodos: this.nodos,
        origenes: this.origenes,
        destinos: this.destinos,
        pesos: this.pesos,
      });
      console.log(this.$store.state);
    },
  },
};
</script>
