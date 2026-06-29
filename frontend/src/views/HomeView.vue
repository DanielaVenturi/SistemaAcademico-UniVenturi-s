<script setup>

import { ref } from "vue";
import { useRouter } from "vue-router";

import {
  listarAlunos,
  buscarPorNome,
  buscarPorCurso,
  buscarPorMatricula,
  ordenarPorNome,
  ordenarPorCurso,
  ordenarPorMatricula
} from "../services/alunoService";

const router = useRouter();

const pesquisa = ref("");
const tipoBusca = ref("nome");

const alunos = ref([]);

const mostrarTodos = ref(false);

const filtro = ref("");

async function pesquisar() {

  mostrarTodos.value = false;

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

  if (tipoBusca.value == "matricula") {

    try{

      const aluno = await buscarPorMatricula(
        pesquisa.value
      );

      alunos.value = [aluno];

    }catch{

      alunos.value=[];

      alert("Aluno não encontrado.");

    }

  }

}

async function alterarTodos(){

  if(mostrarTodos.value){

    alunos.value = await listarAlunos();

  }else{

    alunos.value=[];

    filtro.value="";

  }

}

async function aplicarFiltro(){

  if(filtro.value=="")
    return;

  if(filtro.value=="nomeAZ"){

    alunos.value = await ordenarPorNome();

  }

  if(filtro.value=="cursoAZ"){

    alunos.value = await ordenarPorCurso();

  }

  if(filtro.value=="matricula"){

    alunos.value = await ordenarPorMatricula();

  }

}

function abrirAluno(aluno){

  router.push(`/notas/${aluno.matricula}`);

}

</script>

<template>

<div class="container">

  <h1>Sistema Acadêmico UniVenturi</h1>

  <div class="painel">

    <h2> Buscar Alunos</h2>

    <div class="linha">

      <select v-model="tipoBusca">

        <option value="nome">
          Nome
        </option>

        <option value="curso">
          Curso
        </option>

        <option value="matricula">
          Matrícula
        </option>

      </select>

      <input
        v-model="pesquisa"
        placeholder="Digite sua pesquisa"
        @keyup.enter="pesquisar"
      />

      <button @click="pesquisar">
        Pesquisar
      </button>

    </div>

    <div class="opcoes">

      <label class="todos">

        <input
          type="checkbox"
          v-model="mostrarTodos"
          @change="alterarTodos"
        />

        Mostrar todos

      </label>

      <select
        v-if="alunos.length"
        v-model="filtro"
        @change="aplicarFiltro"
        class="filtro"
      >

        <option value="">
          Filtro
        </option>

        <option value="nomeAZ">
          Nome (A → Z)
        </option>

        <option value="cursoAZ">
          Curso (A → Z)
        </option>

        <option value="matricula">
          Matrícula
        </option>

      </select>

    </div>

  </div>

  <table
    v-if="alunos.length"
    class="tabela"
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
        class="linha-aluno"
        @click="abrirAluno(aluno)"
      >

        <td>{{ aluno.matricula }}</td>

        <td>{{ aluno.nome }}</td>

        <td>{{ aluno.curso }}</td>

      </tr>

    </tbody>

  </table>

  <div
    v-else
    class="vazio"
  >

    Nenhum aluno para exibir.

  </div>

</div>

</template>

<style scoped>

.container{

    max-width:1200px;
    margin:auto;
    padding:35px;

}

h1{

    margin-bottom:30px;
    text-align:center;
    color:#1e3a8a;

}

.painel{

    background:#fff;

    border-radius:12px;

    padding:25px;

    box-shadow:0 2px 10px rgba(0,0,0,.08);

    margin-bottom:25px;

}

.linha{

    display:flex;

    gap:15px;

    align-items:center;

    flex-wrap:wrap;

}

input{

    flex:1;

    min-width:260px;

    padding:12px;

    border:1px solid #ccc;

    border-radius:8px;

    font-size:15px;

}

select{

    padding:12px;

    border:1px solid #ccc;

    border-radius:8px;

    font-size:15px;

}

button{

    padding:12px 18px;

    background:#2563eb;

    color:white;

    border:none;

    border-radius:8px;

    cursor:pointer;

    transition:.2s;

}

button:hover{

    background:#1d4ed8;

}

.opcoes{

    display:flex;

    justify-content:space-between;

    align-items:center;

    margin-top:18px;

    flex-wrap:wrap;

    gap:15px;

}

.todos{

    display:flex;

    align-items:center;

    gap:8px;

    font-size:15px;

}

.filtro{

    width:190px;

}

.tabela{

    width:100%;

    border-collapse:collapse;

    background:white;

    border-radius:10px;

    overflow:hidden;

    box-shadow:0 2px 10px rgba(0,0,0,.08);

}

thead{

    background:#2563eb;

    color:white;

}

th{

    padding:15px;

}

td{

    padding:15px;

    border-bottom:1px solid #eee;

}

.linha-aluno{

    cursor:pointer;

    transition:.2s;

}

.linha-aluno:hover{

    background:#eff6ff;

    transform:scale(1.003);

}

.vazio{

    margin-top:30px;

    text-align:center;

    color:#777;

    font-size:16px;

}

</style>