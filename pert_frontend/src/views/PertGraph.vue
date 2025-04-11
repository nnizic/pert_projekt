<template>
  <div class="p-4">
    <h2 class="text-xl font-semibold mb-4">PERT za "{{ project.name }}"</h2>
    <div v-if="graph">
      <table class="table-auto border w-full text-left">
        <thead class="bg-gray-100">
          <tr>
            <th class="px-4 py-2">Naziv</th>
            <th class="px-4 py-2">ES</th>
            <th class="px-4 py-2">EF</th>
            <th class="px-4 py-2">LS</th>
            <th class="px-4 py-2">LF</th>
            <th class="px-4 py-2">Critical?</th>
          </tr>
        </thead>
        <tbody>
          <tr v-for="(task, id) in graph.tasks" :key="id">
            <td class="px-4 py-2">{{ task.name }}</td>
            <td class="px-4 py-2">{{ task.early_start }}</td>
            <td class="px-4 py-2">{{ task.early_finish }}</td>
            <td class="px-4 py-2">{{ task.late_start }}</td>
            <td class="px-4 py-2">{{ task.late_finish }}</td>
            <td class="px-4 py-2">
              <span
                class="px-2 py-1 text-xs rounded font-bold"
                :class="isCritical(id) ? 'bg-red-500 text-white' : 'bg-gray-200'"
              >
                {{ isCritical(id) ? "Da" : "Ne" }}
              </span>
            </td>
          </tr>
        </tbody>
      </table>
    </div>
    <div v-else>Učitavanje grafa...</div>
  </div>
</template>

<script setup>
import { ref, watch, onMounted } from "vue";
import { getProjectPert } from "../api";

const props = defineProps({
  project: Object,
});

const graph = ref(null);

const loadGraph = async () => {
  const res = await getProjectPert(props.project.id);
  graph.value = res.data;
};

onMounted(loadGraph);
watch(() => props.project, loadGraph);

const isCritical = (id) => {
  return graph.value?.critical_path?.includes(parseInt(id));
};
</script>

