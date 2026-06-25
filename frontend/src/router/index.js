import { createRouter, createWebHistory } from "vue-router";

import HomeView from "../views/HomeView.vue";
import CadastrosView from "../views/CadastrosView.vue";
import ConsultasView from "../views/ConsultasView.vue";
import NotasView from "../views/NotasView.vue";

const routes = [
  {
    path: "/",
    component: HomeView
  },
  {
    path: "/cadastros",
    component: CadastrosView
  },
  {
    path: "/consultas",
    component: ConsultasView
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