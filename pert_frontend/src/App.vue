<template>
  <div class="min-h-screen bg-gray-50">
    <ProjectList @select="selectedProject = $event" />
    <PertGraph v-if="selectedProject" :project="selectedProject" />
  </div>
</template>

<script setup>
import { ref } from "vue";
import ProjectList from "./views/ProjectList.vue";
import PertGraph from "./views/PertGraph.vue";

const selectedProject = ref(null);
</script>

