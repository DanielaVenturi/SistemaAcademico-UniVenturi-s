<script setup>

import { ref, onMounted, onUnmounted } from "vue";

import {
  listarCursos,
  excluirCurso
} from "../services/cursoService";

import EditarCursoModal from "./EditarCursoModal.vue";

const cursos = ref([]);

const modalAberto = ref(false);
const cursoSelecionado = ref(null);

async function carregarCursos() {
  cursos.value = await listarCursos();
}

async function excluir(id){

  if(!confirm("Deseja excluir este curso?"))
    return;

  await excluirCurso(id);

  carregarCursos();

}

function abrirModal(curso){

  cursoSelecionado.value = curso;

  modalAberto.value = true;

}

function atualizar(){

  carregarCursos();

}

onMounted(()=>{

  carregarCursos();

  window.addEventListener(
    "cursoAtualizado",
    atualizar
  );

});

onUnmounted(()=>{

  window.removeEventListener(
    "cursoAtualizado",
    atualizar
  );

});

</script>

<template>

<h2>Lista de Cursos</h2>

<table border="1">

<thead>

<tr>

<th>ID</th>
<th>Nome</th>
<th>Ações</th>

</tr>

</thead>

<tbody>

<tr
v-for="curso in cursos"
:key="curso.id"
>

<td>{{curso.id}}</td>

<td>{{curso.nome}}</td>

<td>

<button
@click="abrirModal(curso)"
>

Editar

</button>

<button
@click="excluir(curso.id)"
>

Excluir

</button>

</td>

</tr>

</tbody>

</table>

<EditarCursoModal

:aberto="modalAberto"

:curso="cursoSelecionado"

@fechar="modalAberto=false"

@atualizado="carregarCursos"

/>

</template>