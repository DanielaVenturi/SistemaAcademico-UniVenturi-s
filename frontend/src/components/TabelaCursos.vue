<script setup>

import { ref, onMounted } from "vue";
import {
  listarCursos,
  excluirCurso
} from "../services/cursoService";

const cursos = ref([]);

async function carregarCursos() {
  cursos.value = await listarCursos();
}

async function excluir(id) {

  if (!confirm("Deseja excluir este curso?")) {
    return;
  }

  await excluirCurso(id);

  carregarCursos();
}

onMounted(() => {
  carregarCursos();
});

</script>

<template>

  <h2>Lista de Cursos</h2>

  <table border="1">

    <thead>

      <tr>
        <th>ID</th>
        <th>Nome</th>
        <th>Ações</th>
      </tr>

    </thead>

    <tbody>

      <tr
        v-for="curso in cursos"
        :key="curso.id"
      >

        <td>{{ curso.id }}</td>

        <td>{{ curso.nome }}</td>

        <td>

          <button
            @click="excluir(curso.id)"
          >
            Excluir
          </button>

        </td>

      </tr>

    </tbody>

  </table>

</template>