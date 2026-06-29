<script setup>

import { ref, onMounted } from "vue";
import { useRoute, useRouter } from "vue-router";

import { buscarPorMatricula } from "../services/alunoService";

const route = useRoute();
const router = useRouter();

const aluno = ref(null);

async function carregarAluno(){

    try{

        aluno.value = await buscarPorMatricula(
            route.params.matricula
        );

    }catch{

        alert("Aluno não encontrado.");

        router.push("/");

    }

}

onMounted(() => {

    carregarAluno();

});

</script>

<template>

<div class="container">

<button
class="voltar"
@click="router.push('/')"
>

← Voltar

</button>

<div
v-if="aluno"
class="card"
>

<h1>

👨‍🎓 {{ aluno.nome }}

</h1>

<p>

<strong>Matrícula:</strong>

{{ aluno.matricula }}

</p>

<p>

<strong>Curso:</strong>

{{ aluno.curso }}

</p>

<hr>

<h2>

📊 Lançamento de Notas

</h2>

<p>

(Em instantes vamos colocar os campos de notas aqui.)

</p>

</div>

</div>

</template>

<style scoped>
.container{

    max-width:900px;

    margin:auto;

    padding:35px;

}

.voltar{

    margin-bottom:25px;

    padding:10px 18px;

    border:none;

    border-radius:8px;

    background:#2563eb;

    color:white;

    cursor:pointer;

}

.card{

    background:white;

    padding:30px;

    border-radius:12px;

    box-shadow:0 2px 10px rgba(0,0,0,.08);

}

h1{

    margin-top:0;

}

p{

    font-size:17px;

}

hr{

    margin:30px 0;

}
</style>