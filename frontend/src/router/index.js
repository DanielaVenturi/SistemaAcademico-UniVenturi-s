import { createRouter, createWebHistory } from "vue-router";

import HomeView from "../views/HomeView.vue";
import CursosView from "../views/CursosView.vue";
import AlunosView from "../views/AlunosView.vue";
import NotasView from "../views/NotasView.vue";

const routes = [
  {
    path: "/",
    component: HomeView
  },
  {
    path: "/cursos",
    component: CursosView
  },
  {
    path: "/alunos",
    component: AlunosView
  },
  {
    path: "/notas",
    component: NotasView
  }
];

const router = createRouter({
  history: createWebHistory(),
  routes
});

export default router;