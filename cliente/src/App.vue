<template>
  <div
    class="is-flex"
    style="justify-content: center;
    align-items: center;
    height: 100%; padding: 40px;"
  >
    <Main />
  </div>
</template>

<script>
import Main from "./views/Main.vue";

export default {
  name: "App",
  components: {
    Main,
  },
};
</script>

<style>
html,
body {
  height: 100%;
  min-height: 100%;
}

body {
  background-color: #7958d5;
}

.is-full-h {
  height: 100% !important;
}
</style>
