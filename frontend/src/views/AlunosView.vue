<template>
  <div>

    <Navbar />

    <h1>Alunos</h1>

    <h2>Cadastrar Aluno</h2>

    <form @submit.prevent="salvarAluno">

      <input
        v-model="novoAluno.matricula"
        type="number"
        placeholder="Matrícula"
      />

      <input
        v-model="novoAluno.nome"
        placeholder="Nome"
      />

      <select v-model="novoAluno.curso_id">

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

     <button type="submit">

  {{ editando
      ? "Atualizar"
      : "Salvar" }}

</button>

    </form>

    <hr>

    <table border="1">

      <thead>
        <tr>
          <th>Matrícula</th>
          <th>Nome</th>
          <th>Curso</th>
          <th>Ações</th>
        </tr>
      </thead>

      <tbody>

        <tr
          v-for="aluno in alunos"
          :key="aluno.matricula"
        >

          <td>{{ aluno.matricula }}</td>
          <td>{{ aluno.nome }}</td>
          <td>{{ aluno.curso }}</td>

          <td>
<button
  @click="editarAluno(aluno)"
>
  Editar
</button>
            <button
              @click="removerAluno(
                aluno.matricula
              )"
            >
              Excluir
            </button>

          </td>

        </tr>

      </tbody>

    </table>

  </div>
</template>

<script setup>

import { ref, onMounted }
from "vue";

import Navbar
from "../components/Navbar.vue";

import {
  listarAlunos,
  cadastrarAluno,
  excluirAluno,
  atualizarAluno
}
from "../services/alunoService";

import {
  listarCursos
}
from "../services/cursoService";

const alunos = ref([]);

const cursos = ref([]);
const editando = ref(false);

const matriculaEdicao = ref(null);
const novoAluno = ref({
  matricula: "",
  nome: "",
  curso_id: ""
});

async function carregarAlunos() {

  alunos.value =
    await listarAlunos();

}

async function carregarCursos() {

  cursos.value =
    await listarCursos();

}

async function salvarAluno() {

  if (editando.value) {

    await atualizarAluno(
      matriculaEdicao.value,
      {
        nome: novoAluno.value.nome,
        curso_id: novoAluno.value.curso_id
      }
    );

  } else {

    await cadastrarAluno(
      novoAluno.value
    );

  }

  novoAluno.value = {
    matricula: "",
    nome: "",
    curso_id: ""
  };

  editando.value = false;

  matriculaEdicao.value = null;

  await carregarAlunos();
}

async function removerAluno(matricula) {

  await excluirAluno(matricula);

  await carregarAlunos();
}

function editarAluno(aluno) {

  editando.value = true;

  matriculaEdicao.value =
    aluno.matricula;

  const cursoSelecionado =
    cursos.value.find(
      c => c.nome === aluno.curso
    );

  novoAluno.value = {
    matricula: aluno.matricula,
    nome: aluno.nome,
    curso_id: cursoSelecionado
      ? cursoSelecionado.id
      : ""
  };

}
onMounted(async () => {

  await carregarCursos();

  await carregarAlunos();

});

</script>