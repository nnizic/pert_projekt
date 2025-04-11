<template>
  <div class="p-4">
    <h1 class="text-2xl font-bold mb-4">Projekti</h1>
    <ul class="space-y-2">
      <li v-for="project in projects" :key="project.id">
        <button
          class="bg-blue-500 text-white px-4 py-2 rounded hover:bg-blue-600"
          @click="$emit('select', project)"
        >
          {{ project.name }}
        </button>
      </li>
    </ul>
  </div>
</template>

<script setup>
import { ref, onMounted } from "vue";
import { getProjects } from "../api";

const projects = ref([]);

onMounted(async () => {
  const res = await getProjects();
  projects.value = res.data;
});
</script>

