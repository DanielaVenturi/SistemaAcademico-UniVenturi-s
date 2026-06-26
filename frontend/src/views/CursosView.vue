<script setup>

import CursoForm from "../components/CursoForm.vue";
import TabelaCursos from "../components/TabelaCursos.vue";
import { useRouter } from "vue-router";

const router = useRouter();

</script>

<template>

  <div class="container">

    <button
      class="voltar"
      @click="router.push('/cadastros')"
    >
      ← Voltar
    </button>

    <h1>📚 Gerenciamento de Cursos</h1>

    <CursoForm />

    <br>

    <TabelaCursos />

  </div>

</template>

<style scoped>

.container{
    padding:30px;
}

.voltar{
    padding:10px 18px;
    cursor:pointer;
    margin-bottom:20px;
}

</style>