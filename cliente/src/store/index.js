import Vue from "vue";
import Vuex from 'vuex';

Vue.use(Vuex);

const store = new Vuex.Store({
    state: {
        nodos: [],
        origenes: [],
        destinos: [],
        pesos: []
    },
    mutations: {
        crearGrafo(state, payload) {
            state.nodos = payload.nodos;
            state.origenes = payload.origenes;
            state.destinos = payload.destinos;
            state.pesos = payload.pesos;
        }
    },
    getters: {
        grafo: state => {
            var aristas = [];
            var vertices = [];

            for (const nodo of state.nodos) {
                vertices.push(nodo.etiqueta);
            }

            for (let i = 0; i < state.origenes.length; i++) {
                const origen = state.origenes[i];
                const destino = state.destinos[i];
                const peso = state.pesos[i];

                aristas.push({
                    inicio: origen,
                    final: destino,
                    peso: peso,
                });
            }
            return {
                aristas,
                vertices
            };
        }
    }
});

export default store;