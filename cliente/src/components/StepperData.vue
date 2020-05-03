<template>
  <section class="is-full-h">
    <b-steps
      size="is-small"
      class="is-full-h"
      v-model="pasoActual"
      :animated="true"
      :rounded="true"
      :has-navigation="true"
      :icon-prev="prevIcon"
      :icon-next="nextIcon"
    >
      <b-step-item
        step="1"
        label="Nodos"
        :clickable="false"
        class="is-full-h"
        style="border-bottom: 2px solid #f5f5f5; border-top: 2px solid #f5f5f5;"
      >
        <nodos-input :nodos="nodos" />
      </b-step-item>

      <b-step-item
        step="2"
        class="is-full-h"
        label="Aristas"
        style="border-bottom: 2px solid #f5f5f5; border-top: 2px solid #f5f5f5;"
        :clickable="false"
        :type="{ 'is-success': false }"
      >
        <aristas-input :nodos="nodos" />
      </b-step-item>
    </b-steps>
  </section>
</template>

<style>
.b-steps .steps,
.b-steps .step-navigation {
  padding: 10px;
}

.b-steps .step-navigation {
  padding-left: 20px;
  padding-right: 20px;
}
.step-content {
  padding: 0 !important;
  height: calc(100% - 77px - 64px);
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
