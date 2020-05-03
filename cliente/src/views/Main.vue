<template>
  <div class="is-flex" style="width: 100%;">
    <div
      class="card"
      style="width: 100%; height: calc(100vh - 80px); border-radius: 20px;"
    >
      <div class="card-content is-full-h">
        <div class="content is-full-h">
          <stepper-data />
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import StepperData from "../components/StepperData.vue";

export default {
  name: "Main",
  components: {
    StepperData,
  },
  data: () => ({}),
};
</script>
