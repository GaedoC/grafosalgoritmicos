<template>
  <div class="hello is-primary">
    <section class="hero is-primary">
      <div class="hero-body">
        <div class="container">
          <h1 class="title">
            Que tal gente del yutub
          </h1>
          <h2 class="subtitle">
            Bienvenidos a un nuevo video de Minecraft 1.8
          </h2>
        </div>
      </div>
    </section>
    <div class="columns" style="align-items: flex-end; padding: 20px;">
      <div class="column" style="padding: 20px;">
        <nodos-input />
      </div>
      <div class="column"></div>
    </div>
  </div>
</template>

<script>
import NodosInput from "../components/NodosInput.vue";

export default {
  name: "Main",
  components: {
    NodosInput,
  },
};
</script>
