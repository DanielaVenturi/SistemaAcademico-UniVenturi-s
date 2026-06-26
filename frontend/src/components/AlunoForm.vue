<script setup>

import { ref, onMounted } from "vue";

import { cadastrarAluno } from "../services/alunoService";
import { listarCursos } from "../services/cursoService";

const matricula = ref("");
const nome = ref("");
const curso_id = ref("");

const cursos = ref([]);

async function carregarCursos() {
  cursos.value = await listarCursos();
}

async function salvarAluno() {
  alert("Cliquei!");
  if (!matricula.value || !nome.value || !curso_id.value) {
    alert("Preencha todos os campos.");
    return;
  }

  try {

    console.log("Enviando:", {
      matricula: Number(matricula.value),
      nome: nome.value,
      curso_id: Number(curso_id.value)
    });

    const resposta = await cadastrarAluno({
      matricula: Number(matricula.value),
      nome: nome.value,
      curso_id: Number(curso_id.value)
    });

    console.log("Resposta:", resposta);

    alert("Aluno cadastrado com sucesso!");

    matricula.value = "";
    nome.value = "";
    curso_id.value = "";

  } catch (erro) {

    console.error("Erro:", erro);

    if (erro.response) {
      console.log("Status:", erro.response.status);
      console.log("Resposta:", erro.response.data);
    }

    alert("Erro ao cadastrar aluno.");

  }

}

onMounted(() => {
  carregarCursos();
});

</script>

<template>

  <h2>Cadastrar Aluno</h2>

  <input
    v-model="matricula"
    placeholder="Matrícula"
  />

  <br><br>

  <input
    v-model="nome"
    placeholder="Nome"
  />

  <br><br>

  <select v-model="curso_id">

    <option value="">
      Selecione um curso
    </option>

    <option
      v-for="curso in cursos"
      :key="curso.id"
      :value="curso.id"
    >
      {{ curso.nome }}
    </option>

  </select>

  <br><br>

  <button @click="salvarAluno">
    Salvar
  </button>

</template>