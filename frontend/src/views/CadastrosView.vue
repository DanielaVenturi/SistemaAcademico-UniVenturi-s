<script setup>

import { ref } from "vue";

import CursoForm from "../components/CursoForm.vue";
import TabelaCursos from "../components/TabelaCursos.vue";

import AlunoForm from "../components/AlunoForm.vue";
import TabelaAlunos from "../components/TabelaAlunos.vue";

import ResumoAlunos from "../components/ResumoAlunos.vue";
import ResumoCursos from "../components/ResumoCursos.vue";

const telaAtual = ref("");

</script>

<template>

  <div class="container">

    <h1>📝 Cadastros</h1>

    <!-- Tela inicial -->
    <div v-if="telaAtual === ''">

      <div class="resumos">

        <ResumoAlunos />

        <ResumoCursos />

      </div>

      <div class="acoes">

        <button
          @click="telaAtual = 'alunos'"
        >
          👨‍🎓 Gerenciar Alunos
        </button>

        <button
          @click="telaAtual = 'cursos'"
        >
          📚 Gerenciar Cursos
        </button>

      </div>

    </div>

    <!-- Tela de Cursos -->
    <div v-if="telaAtual === 'cursos'">

      <button
        @click="telaAtual = ''"
      >
        ← Voltar
      </button>

      <h2>📚 Gerenciamento de Cursos</h2>

      <CursoForm />

      <TabelaCursos />

    </div>

    <!-- Tela de Alunos -->
    <div v-if="telaAtual === 'alunos'">

      <button
        @click="telaAtual = ''"
      >
        ← Voltar
      </button>

      <h2>👨‍🎓 Gerenciamento de Alunos</h2>

      <AlunoForm />

      <TabelaAlunos />

    </div>

  </div>

</template>

<style scoped>

.container{
  padding:30px;
}

.resumos{
  display:flex;
  gap:20px;
  margin:25px 0;
  flex-wrap:wrap;
}

.acoes{
  margin-top:20px;
}

button{
  padding:10px 18px;
  margin-right:10px;
  cursor:pointer;
}

</style>