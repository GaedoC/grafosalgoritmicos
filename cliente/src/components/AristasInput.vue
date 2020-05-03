<template>
  <div>
    <div class="columns is-marginless is-paddingless">
      <div class="column is-6">
        <b-field
          grouped
          v-for="(origen, i) in origenes"
          :key="i"
          class="columns"
        >
          <b-field class="column" :label="'Peso ' + (i + 1)">
            <b-select placeholder="Nodo de origen">
              <option v-for="nodo in nodos" :value="nodo" :key="nodo">
                {{ nodo }}
              </option>
            </b-select>
          </b-field>
          <b-field class="column" :label="'Peso ' + (i + 1)">
            <b-select placeholder="Nodo de origen">
              <option v-for="nodo in nodos" :value="nodo" :key="nodo">
                {{ nodo }}
              </option>
            </b-select>
          </b-field>
          <b-field :label="'Peso ' + (i + 1)" class="column">
            <b-numberinput
              controls-position="compact"
              controls-rounded
              expanded
              style="width: 150px"
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
        <div class="is-marginless is-paddingless">
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
      <div class="column is-6">
        <pre>
          <code class="language-javascript">{{ grafo }}</code>
        </pre>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: "AristasInput",
  data: () => ({
    nodos: ["A", "B", "C", "D"],
    origenes: [null],
    destinos: [null],
    pesos: [0],
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
      this.pesos.push(0);
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
