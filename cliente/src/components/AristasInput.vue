<template>
  <div>
    <div
      class="columns is-marginless is-paddingless"
      style="align-items: flex-end;"
      v-for="(origen, i) in origenes"
      :key="i"
    >
      <b-field grouped>
        <b-field
          :label="'Origen ' + (i + 1)"
          :type="validarNodo(origenes[i]) ? 'is-danger' : ''"
          :message="validarNodo(origenes[i])"
        >
          <b-autocomplete
            v-model="origenes[i]"
            :data="getNodosFiltrados(origenes[i])"
            keep-first
            expanded
            clearable
            open-on-focus
            placeholder="Nodo de origen"
            rounded
          ></b-autocomplete>
        </b-field>

        <b-field
          :label="'Destino ' + (i + 1)"
          :type="validarNodo(destinos[i]) ? 'is-danger' : ''"
          :message="validarNodo(destinos[i])"
        >
          <b-autocomplete
            v-model="destinos[i]"
            :data="nodos"
            clearable
            expanded
            open-on-focus
            keep-first
            placeholder="Nodo de destino"
            rounded
          ></b-autocomplete>
        </b-field>
        <b-field :label="'Peso ' + (i + 1)">
          <b-numberinput
            controls-position="compact"
            controls-rounded
            expanded
            min="0"
            v-model="pesos[i]"
          >
          </b-numberinput>
        </b-field>

        <b-tooltip
          v-if="origenes.length > 1"
          label="Eliminar"
          class="is-danger"
          position="is-right"
          style="margin-top: 20px;"
        >
          <a class="navbar-item control" @click="eliminarArista(i)"
            ><b-icon pack="fa" class="is-danger" icon="minus-circle"></b-icon
          ></a>
        </b-tooltip>
        <div v-else class="navbar-item control" style="margin-top: 20px;">
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
        @click="agregarArista"
        icon-left="plus-circle"
        >Agregar arista</b-button
      >
    </div>

    <pre>
    <code class="language-javascript">{{ grafo }}</code>
    </pre>
  </div>
</template>

<script>
export default {
  name: "AristasInput",
  data: () => ({
    nodos: ["A", "B", "C", "D"],
    origenes: [null],
    destinos: [null],
    pesos: [null],
  }),
  computed: {
    grafo() {
      var aristas = [];
      for (let i = 0; i < this.origenes.length; i++) {
        const origen = this.origenes[i];
        const destino = this.destinos[i];
        const peso = this.pesos[i];

        aristas.push({
          inicio: origen,
          final: destino,
          peso: peso,
        });
      }
      return {
        grafo: aristas,
      };
    },
  },
  methods: {
    agregarArista() {
      this.origenes.push(null);
      this.destinos.push(null);
      this.pesos.push(null);
    },
    eliminarArista(i) {
      this.origenes.splice(i, 1);
      this.destinos.splice(i, 1);
      this.pesos.splice(i, 1);
    },
    validarNodo(valor) {
      if (valor != null) {
        if (this.nodos.indexOf(valor) < 0) {
          return "Debe seleccionar un nodo válido";
        }
      }
      return null;
    },
    getNodosFiltrados(valor) {
      if (valor != null) {
        return this.nodos.filter((n) => {
          n.toString()
            .toLowerCase()
            .includes(valor.toString().toLowerCase);
        });
      }
      return this.nodos;
    },
  },
};
</script>
