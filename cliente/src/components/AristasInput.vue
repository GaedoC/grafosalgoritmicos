<template>
  <div>
    <div
      class="columns is-marginless is-paddingless"
      style="align-items: flex-end;"
      v-for="(origen, i) in origenes"
      :key="i"
    >
      <div class="column">
        <b-field :label="'Origen ' + (i + 1)">
          <b-autocomplete
            v-model="origenes[i]"
            :data="nodos"
            placeholder=""
            rounded
          ></b-autocomplete>
        </b-field>
      </div>
      <div class="column">
        <b-field :label="'Destino ' + (i + 1)">
          <b-autocomplete
            v-model="destinos[i]"
            :data="nodos"
            placeholder=""
            rounded
          ></b-autocomplete>
        </b-field>
      </div>
      <div class="column">
        <b-field :label="'Peso ' + (i + 1)">
          <b-input v-model="pesos[i]" placeholder="" rounded></b-input>
        </b-field>
      </div>
      <div class="column is-narrow">
        <b-tooltip
          v-if="origenes.length > 1"
          label="Eliminar"
          class="is-danger"
          position="is-right"
        >
          <a class="navbar-item" @click="eliminarArista(i)"
            ><b-icon pack="fa" class="is-danger" icon="minus-circle"></b-icon
          ></a>
        </b-tooltip>
        <div v-else class="navbar-item">
          <b-icon pack="fa" icon="minus-circle" style="color: grey;"></b-icon>
        </div>
      </div>
    </div>
    <div
      class="columns is-marginless is-paddingless"
      style="align-items: flex-end;"
    >
      <b-button
        type="is-primary"
        style=" margin: 12px;"
        outlined
        rounded
        expanded
        @click="agregarArista"
        icon-left="plus-circle"
        >Agregar arista</b-button
      >
    </div>
  </div>
</template>

<script>
export default {
  name: "AristasInput",
  data: () => ({
    nodos: ["A", "B", "C", "D"],
    origenes: [null],
    destinos: [],
    pesos: [],
  }),
  methods: {
    agregarArista() {
      this.origenes.push(null);
    },
    eliminarArista(i) {
      this.origenes.splice(i, 1);
      this.destinos.splice(i, 1);
      this.pesos.splice(i, 1);
    },
  },
};
</script>
