<script setup>
import { ref, onMounted } from "vue";
import { listarAlunos, excluirAluno } from "../services/alunoService";

const alunos = ref([]);

async function carregarAlunos() {
  alunos.value = await listarAlunos();
}

async function excluir(matricula) {

  const confirmar = confirm(
    "Deseja excluir este aluno?"
  );

  if (!confirmar) return;

  await excluirAluno(matricula);

  carregarAlunos();
}

onMounted(() => {
  carregarAlunos();
});
</script>

<template>

  <h2>Lista de Alunos</h2>

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

          <button>
            Editar
          </button>

          <button
            @click="excluir(aluno.matricula)"
          >
            Excluir
          </button>

        </td>

      </tr>

    </tbody>

  </table>

</template>