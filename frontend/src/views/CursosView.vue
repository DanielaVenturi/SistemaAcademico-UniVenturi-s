<template>
  <div>

    <Navbar />

    <h1>Cursos</h1>

    <form @submit.prevent="salvarCurso">

      <input
        v-model="novoCurso"
        placeholder="Nome do curso"
      />

      <button type="submit">
        Cadastrar
      </button>

    </form>

    <hr>

    <ul>

      <li
        v-for="curso in cursos"
        :key="curso.id"
      >

        {{ curso.nome }}

        <button @click="removerCurso(curso.id)">
          Excluir
        </button>

      </li>

    </ul>

  </div>
</template>

<script setup>

import { ref, onMounted } from "vue";

import Navbar from "../components/Navbar.vue";

import {
  listarCursos,
  cadastrarCurso,
  excluirCurso
}
from "../services/cursoService";

const cursos = ref([]);

const novoCurso = ref("");

async function carregarCursos() {

  cursos.value = await listarCursos();

}

async function salvarCurso() {

  if (!novoCurso.value.trim()) return;

  await cadastrarCurso(
    novoCurso.value
  );

  novoCurso.value = "";

  await carregarCursos();
}

async function removerCurso(id) {

  await excluirCurso(id);

  await carregarCursos();
}

onMounted(() => {

  carregarCursos();

});

</script>