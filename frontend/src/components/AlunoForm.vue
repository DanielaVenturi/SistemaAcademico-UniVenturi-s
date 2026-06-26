<script setup>
import { ref, onMounted } from "vue";
import { useRouter } from "vue-router";

import { cadastrarAluno } from "../services/alunoService";
import { listarCursos } from "../services/cursoService";

const emit = defineEmits(["alunoCadastrado"]);

const matricula = ref("");
const nome = ref("");
const curso_id = ref("");

const cursos = ref([]);

async function carregarCursos() {
  cursos.value = await listarCursos();
}

async function salvarAluno() {

  if (!matricula.value || !nome.value || !curso_id.value) {
    alert("Preencha todos os campos.");
    return;
  }

  try {

    await cadastrarAluno({
      matricula: Number(matricula.value),
      nome: nome.value,
      curso_id: Number(curso_id.value)
    });

    alert("Aluno cadastrado com sucesso!");

    matricula.value = "";
    nome.value = "";
    curso_id.value = "";

    emit("alunoCadastrado");

  } catch (erro) {

    console.error(erro);

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