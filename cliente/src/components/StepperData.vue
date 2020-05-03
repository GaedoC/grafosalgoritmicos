<template>
  <section class="is-full-h">
    <b-steps
      class="is-full-h"
      v-model="pasoActual"
      :animated="true"
      :rounded="true"
      :has-navigation="true"
      :icon-prev="prevIcon"
      :icon-next="nextIcon"
    >
      <b-step-item step="1" label="Nodos" :clickable="false" class="is-full-h">
        <nodos-input :nodos="nodos" />
      </b-step-item>

      <b-step-item
        step="2"
        class="is-full-h"
        label="Aristas"
        :clickable="false"
        :type="{ 'is-success': false }"
      >
        <aristas-input :nodos="nodos" />
      </b-step-item>
    </b-steps>
  </section>
</template>

<style>
.step-content {
  height: calc(100% - 104px);
}
</style>

<script>
import AristasInput from "./AristasInput.vue";
import NodosInput from "./NodosInput.vue";

export default {
  name: "StepperData",
  components: {
    AristasInput,
    NodosInput,
  },
  data() {
    return {
      pasoActual: 0,
      prevIcon: "chevron-left",
      nextIcon: "chevron-right",
      nodos: ["A"],
    };
  },
};
</script>
