<template>
    <section>
        <b-steps
            v-model="pasoActual"
            :animated="true"
            :rounded="true"
            :has-navigation="true"
            :icon-prev="prevIcon"
            :icon-next="nextIcon">
            <b-step-item step="1" label="Nodos" :clickable="false">
                <h1 class="title has-text-centered">Nodos</h1>
                <nodos-input/>
            </b-step-item>

            <b-step-item step="2" label="Aristas" :clickable="false" :type="{'is-success': false}">
                <h1 class="title has-text-centered">Aristas</h1>
                <div style="padding: 20px;">
                <aristas-input />
                </div>
            </b-step-item>
        </b-steps>
    </section>
</template>

<script>
    import AristasInput from "./AristasInput.vue";
    import NodosInput from "./NodosInput.vue";

    export default {
        name: "StepperData",
        components: {
            AristasInput,
            NodosInput
        },
        data() {
            return {
                pasoActual: 0,
                prevIcon: 'chevron-left',
                nextIcon: 'chevron-right',
            }
        }
    }
</script>