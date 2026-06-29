<script setup>

import { ref } from "vue";

import { cadastrarCurso } from "../services/cursoService";

const emit = defineEmits([
    "cursoCadastrado"
]);

const nome = ref("");

async function salvar(){

    if(nome.value.trim()==""){

        alert("Informe o nome do curso.");

        return;

    }

    try{

        const resposta = await cadastrarCurso({

            nome:nome.value

        });

        if(resposta.erro){

            alert(resposta.erro);

            return;

        }

        alert("Curso cadastrado com sucesso!");

        nome.value="";

        emit("cursoCadastrado");

    }catch{

        alert("Erro ao cadastrar curso.");

    }

}

</script>

<template>

<div class="card">

    <h3>

        Cadastro de Curso

    </h3>

    <div class="grid">

        <div>

            <label>

                Nome do Curso

            </label>

            <input
                v-model="nome"
                type="text"
                placeholder="Ex.: Engenharia de Software"
            >

        </div>

    </div>

    <button @click="salvar">

        Salvar Curso

    </button>

</div>

</template>

<style scoped>

.card{

    background:white;
    padding:30px;
    border-radius:14px;
    box-shadow:0 4px 15px rgba(0,0,0,.08);
    margin-bottom:30px;

}

h3{

    margin-top:0;
    margin-bottom:25px;
    color:#1e3a8a;

}

.grid{

    display:grid;

}

label{

    display:block;
    margin-bottom:8px;
    font-weight:600;

}

input{

    width:100%;
    padding:12px;
    border:1px solid #d1d5db;
    border-radius:10px;
    font-size:15px;
    box-sizing:border-box;

}

input:focus{

    outline:none;
    border-color:#2563eb;

}

button{

    margin-top:25px;
    padding:12px 25px;
    border:none;
    border-radius:10px;
    background:#2563eb;
    color:white;
    cursor:pointer;

}

button:hover{

    background:#1d4ed8;

}

</style>