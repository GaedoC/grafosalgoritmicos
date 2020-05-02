<template>
  <div>
    <div class="columns" style="padding: 20px;">
      <div class="column is-6" style="padding: 20px;">
        <aristas-input />
      </div>
      <div class="column is-6 is-paddingless" style="border: 1px solid grey;">
        <cytoscape ref="cy" :config="config">
          <cy-element
            v-for="def in elements"
            :key="`${def.data.id}`"
            :definition="def"
          />
        </cytoscape>
      </div>
    </div>
  </div>
</template>

<script>
import AristasInput from "../components/AristasInput.vue";

export default {
  name: "Main",
  components: {
    AristasInput,
  },
  data: () => ({
    config: {
      zoom: 4,
      elements: [
        {
          data: { id: "a" },
          group: "nodes",
        },
        {
          data: { id: "b" },
          group: "nodes",
        },
        {
          data: { id: "c" },
          group: "nodes",
        },
        {
          data: { id: "ab", source: "a", target: "b" },
          group: "edges",
        },
      ],
      style: [
        {
          selector: "node",
          style: { "background-color": "#666", label: "data(id)" },
        },
        {
          selector: "edge",
          style: {
            width: 3,
            "line-color": "#ccc",
            "target-arrow-color": "#ccc",
            "target-arrow-shape": "triangle",
          },
        },
      ],
      layout: { name: "circle", rows: 1 },
    },
  }),
  mounted() {
    document.getElementById("cytoscape-div").style.minHeight = "100vh";
    document.getElementById("cytoscape-div").style.height = "100%";
  },
};
</script>
