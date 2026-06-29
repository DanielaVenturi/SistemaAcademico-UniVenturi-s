import { createRouter, createWebHistory } from "vue-router";

import HomeView from "../views/HomeView.vue";
import CadastrosView from "../views/CadastrosView.vue";
import ConsultasView from "../views/ConsultasView.vue";
import NotasView from "../views/NotasView.vue";
import CursosView from "../views/CursosView.vue";
import AlunoDetalhesView from "../views/AlunoDetalhesView.vue";
import RelatoriosView from "../views/RelatoriosView.vue";
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
  },
  {
    path: "/notas/:matricula",
    component: AlunoDetalhesView
  },
  {
  path: "/relatorios",
  component: RelatoriosView
},
  {
    path: "/cursos",
    component: CursosView
  }
];

export default createRouter({
    history: createWebHistory(),
    routes
});