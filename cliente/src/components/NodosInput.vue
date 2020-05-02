<template>
  <div>
    <div
      class="columns is-marginless is-paddingless"
      style="align-items: flex-end;"
      v-for="(etiqueta, i) in etiquetas"
      :key="i"
    >
      <b-field grouped>
        <b-field :label="'Etiqueta nodo ' + (i + 1)">
          <b-input v-model="etiquetas[i]" placeholder="" rounded></b-input>
        </b-field>
        <b-tooltip
          v-if="etiquetas.length > 1"
          label="Eliminar"
          class="is-danger"
          position="is-right"
        >
          <a class="navbar-item" @click="eliminarNodo(i)"
            ><b-icon pack="fa" class="is-danger" icon="minus-circle"></b-icon
          ></a>
        </b-tooltip>
        <div v-else class="navbar-item">
          <b-icon pack="fa" icon="minus-circle" style="color: grey;"></b-icon>
        </div>
      </b-field>
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
        @click="agregarNodo"
        icon-left="plus-circle"
        >Agregar nodo</b-button
      >
    </div>
  </div>
</template>

<script>
export default {
  name: "NodosInput",
  data: () => ({
    etiquetas: ["A"],
    indiceMaximo: 1,
  }),
  methods: {
    agregarNodo() {
      this.indiceMaximo++;
      var valorAsciiA = 65;
      var caracter = String.fromCharCode(valorAsciiA + this.indiceMaximo);
      this.etiquetas.push(caracter);
    },
    eliminarNodo(i) {
      this.etiquetas.splice(i, 1);
    },
  },
};
</script>
