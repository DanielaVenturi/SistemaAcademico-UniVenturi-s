<script setup>

import { ref, watch } from "vue";
import { atualizarCurso } from "../services/cursoService";

const props = defineProps({
  aberto: Boolean,
  curso: Object
});

const emit = defineEmits([
  "fechar",
  "atualizado"
]);

const nome = ref("");

watch(
  () => props.curso,
  (novoCurso) => {
    if (!novoCurso) return;
    nome.value = novoCurso.nome;
  }
);

async function salvar() {

  if(nome.value.trim()==""){
    alert("Digite um nome.");
    return;
  }

  await atualizarCurso(
    props.curso.id,
    nome.value
  );

  emit("atualizado");
  emit("fechar");

}

</script>

<template>

<div
  v-if="aberto"
  class="overlay"
>

<div class="modal">

<h2>Editar Curso</h2>

<div class="grupo">

<label>Nome do Curso</label>

<input
v-model="nome"
/>

</div>

<div class="botoes">

<button
class="cancelar"
@click="emit('fechar')"
>

Cancelar

</button>

<button
class="salvar"
@click="salvar"
>

Salvar

</button>

</div>

</div>

</div>

</template>

<style scoped>

.overlay{

position:fixed;
top:0;
left:0;

width:100%;
height:100%;

background:rgba(0,0,0,.45);

display:flex;

justify-content:center;
align-items:center;

z-index:999;

}

.modal{

width:420px;

background:white;

padding:30px;

border-radius:12px;

box-shadow:0 10px 30px rgba(0,0,0,.25);

}

h2{

margin-top:0;
text-align:center;
margin-bottom:25px;

}

.grupo{

display:flex;
flex-direction:column;

margin-bottom:20px;

}

label{

font-weight:bold;
margin-bottom:8px;

}

input{

padding:10px;

border:1px solid #ccc;

border-radius:6px;

font-size:15px;

}

.botoes{

display:flex;

justify-content:flex-end;

gap:10px;

margin-top:20px;

}

.salvar{

background:#4CAF50;

color:white;

border:none;

padding:10px 20px;

border-radius:6px;

cursor:pointer;

}

.cancelar{

background:#e74c3c;

color:white;

border:none;

padding:10px 20px;

border-radius:6px;

cursor:pointer;

}

</style>