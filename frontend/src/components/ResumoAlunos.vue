<script setup>

import { ref, onMounted } from "vue";
import { listarAlunos } from "../services/alunoService";

const alunos = ref([]);

onMounted(async () => {
  alunos.value = await listarAlunos();
});

</script>

<template>

  <div class="card">

    <h2>👨‍🎓 Alunos</h2>

    <h1>{{ alunos.length }}</h1>

    <p>alunos cadastrados</p>

  </div>

</template>

<style scoped>

.card{
  width:220px;
  padding:20px;
  border:1px solid #ccc;
  border-radius:10px;
  text-align:center;
}

</style>