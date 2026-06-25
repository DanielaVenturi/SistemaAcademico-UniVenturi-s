<script setup>

import { ref } from "vue";

import {
  buscarPorNome,
  buscarPorMatricula,
  buscarPorCurso,
  ordenarPorNome,
  ordenarPorMatricula,
  ordenarPorCurso
} from "../services/alunoService";

const pesquisa = ref("");
const tipoBusca = ref("nome");

const alunos = ref([]);

async function pesquisar() {

  if (pesquisa.value === "") return;

  if (tipoBusca.value === "nome") {
    alunos.value = await buscarPorNome(pesquisa.value);
  }

  if (tipoBusca.value === "matricula") {
    try {
      const resultado = await buscarPorMatricula(pesquisa.value);
      alunos.value = [resultado];
    } catch {
      alunos.value = [];
      alert("Aluno não encontrado.");
    }
  }

  if (tipoBusca.value === "curso") {
    alunos.value = await buscarPorCurso(pesquisa.value);
  }

}

async function ordenarNome() {
  alunos.value = await ordenarPorNome();
}

async function ordenarMatricula() {
  alunos.value = await ordenarPorMatricula();
}

async function ordenarCurso() {
  alunos.value = await ordenarPorCurso();
}

</script>

<template>

<div class="container">

<h1>🔎 Consultas</h1>

<h3>Buscar aluno</h3>

<select v-model="tipoBusca">

<option value="nome">
Nome
</option>

<option value="matricula">
Matrícula
</option>

<option value="curso">
Curso
</option>

</select>

<input
v-model="pesquisa"
placeholder="Digite sua pesquisa"
/>

<button
@click="pesquisar"
>
Pesquisar
</button>

<hr>

<h3>Ordenação</h3>

<button
@click="ordenarNome"
>
Nome
</button>

<button
@click="ordenarMatricula"
>
Matrícula
</button>

<button
@click="ordenarCurso"
>
Curso
</button>

<hr>

<table
v-if="alunos.length"
border="1"
>

<thead>

<tr>

<th>Matrícula</th>

<th>Nome</th>

<th>Curso</th>

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

</tr>

</tbody>

</table>

<p v-else>

Nenhum resultado encontrado.

</p>

</div>

</template>

<style scoped>

.container{
padding:30px;
}

input{
padding:10px;
width:250px;
margin-left:10px;
}

select{
padding:10px;
margin-right:10px;
}

button{
padding:10px;
margin-left:10px;
margin-top:10px;
}

table{
margin-top:20px;
border-collapse:collapse;
width:100%;
}

th,
td{
padding:10px;
text-align:left;
}

</style>