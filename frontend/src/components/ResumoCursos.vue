<script setup>

import { ref, onMounted } from "vue";
import { listarCursos } from "../services/cursoService";

const cursos = ref([]);

onMounted(async () => {
  cursos.value = await listarCursos();
});

</script>

<template>

  <div class="card">

    <h2>📚 Cursos</h2>

    <h1>{{ cursos.length }}</h1>

    <p>cursos cadastrados</p>

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