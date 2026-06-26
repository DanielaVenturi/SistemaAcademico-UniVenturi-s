<script setup>

import { ref } from "vue";
import { cadastrarCurso } from "../services/cursoService";

const nome = ref("");

async function salvarCurso(){

    if(nome.value==""){
        alert("Digite o nome do curso.");
        return;
    }

    try{

        await cadastrarCurso(nome.value);

        alert("Curso cadastrado com sucesso!");

        nome.value="";

        window.dispatchEvent(new Event("cursoAtualizado"));

    }catch(e){

        alert("Erro ao cadastrar curso.");

        console.log(e);

    }

}

</script>

<template>

<h2>Cadastrar Curso</h2>

<input
v-model="nome"
placeholder="Nome do curso"
/>

<button
@click="salvarCurso"
>

Salvar

</button>

</template>