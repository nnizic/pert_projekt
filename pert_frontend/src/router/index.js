import { createRouter, createWebHistory } from 'vue-router';
import ProjectList from '../views/ProjectList.vue';
import PertGraph from '../views/PertGraph.vue';

const routes = [
  {
    path: '/',
    name: 'Projects',
    component: ProjectList,
  },
  {
    path: '/project/:id',
    name: 'project',
    component: PertGraph,
    props:true, // omogućuje prijenos parametara preko URl kao props

  },
];

const router = createRouter({
  history: createWebHistory(),
  routes,
});

export default router;

