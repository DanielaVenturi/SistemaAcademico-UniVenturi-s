<template>

<div class="container">

<h1>🎓 Sistema Acadêmico UniVenturi</h1>

<div class="cards">

<div class="card">
👨‍🎓
<h2>Alunos</h2>
<p>0</p>
</div>

<div class="card">
📚
<h2>Cursos</h2>
<p>0</p>
</div>

<div class="card">
📝
<h2>Notas</h2>
<p>0</p>
</div>

<div class="card">
📈
<h2>Média Geral</h2>
<p>0</p>
</div>

</div>

<hr>

<h2>🔎 Buscar Alunos</h2>

<div class="busca">

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

<button @click="pesquisar">
Pesquisar
</button>

</div>

<h2>📋 Ordenação</h2>

<div class="ordenacao">

<button @click="ordenarNome">
Nome
</button>

<button @click="ordenarMatricula">
Matrícula
</button>

<button @click="ordenarCurso">
Curso
</button>

</div>

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

<p
v-else
class="vazio"
>

Nenhum resultado encontrado.

</p>

</div>

</template>

<script setup>

import { ref } from "vue";

import {
  buscarPorNome,
  buscarPorCurso,
  ordenarPorNome,
  ordenarPorCurso
} from "../services/alunoService";

const pesquisa = ref("");

const tipoBusca = ref("nome");

const ordenar = ref("nome");

const alunos = ref([]);

async function pesquisar() {

  if (pesquisa.value.trim() == "") {

    alunos.value = [];

    return;

  }

  if (tipoBusca.value == "nome") {

    alunos.value = await buscarPorNome(
      pesquisa.value
    );

  }

  if (tipoBusca.value == "curso") {

    alunos.value = await buscarPorCurso(
      pesquisa.value
    );

  }

}

async function aplicarOrdenacao(){

  if(ordenar.value=="nome"){

    alunos.value=await ordenarPorNome();

  }

  if(ordenar.value=="curso"){

    alunos.value=await ordenarPorCurso();

  }

}

</script>
<style scoped>

.container{
    padding:30px;
}

.cards{

    display:flex;

    gap:20px;

    margin:30px 0;

    flex-wrap:wrap;

}

.card{

    width:180px;

    border:1px solid #ddd;

    border-radius:12px;

    padding:20px;

    text-align:center;

    box-shadow:0 2px 6px rgba(0,0,0,.12);

}

.busca{

    display:flex;

    gap:10px;

    align-items:center;

    margin:20px 0;

    flex-wrap:wrap;

}

.ordenacao{

    display:flex;

    gap:10px;

    margin:20px 0;

    flex-wrap:wrap;

}

input{

    padding:10px;

    width:280px;

}

select{

    padding:10px;

}

button{

    padding:10px 18px;

    cursor:pointer;

}

table{

    width:100%;

    margin-top:25px;

    border-collapse:collapse;

}

th,
td{

    padding:12px;

    text-align:left;

}

.vazio{

    margin-top:20px;

    color:#666;

}

</style>