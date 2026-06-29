<script setup>

import { ref, onMounted } from "vue";

import {
    cadastrarAluno
} from "../services/alunoService";

import {
    listarCursos
} from "../services/cursoService";

const emit = defineEmits([
    "alunoCadastrado"
]);

const matricula = ref("");
const nome = ref("");
const curso = ref("");

const cursos = ref([]);

async function carregarCursos(){

    cursos.value = await listarCursos();

}

async function salvar(){

   try{

    const resposta = await cadastrarAluno({

        matricula:Number(matricula.value),

        nome:nome.value,

        curso_id:Number(curso.value)

    });

    if(resposta.erro){

        alert(resposta.erro);

        return;

    }

    alert("Aluno cadastrado com sucesso!");

    matricula.value="";
    nome.value="";
    curso.value="";

    emit("alunoCadastrado");

}catch(e){

    alert("Erro ao cadastrar aluno.");

}}

onMounted(()=>{

    carregarCursos();

});

</script>

<template>

<div class="card">

    <h3>

        Cadastro de Aluno

    </h3>

    <div class="grid">

        <div>

            <label>

                Matrícula

            </label>

            <input
                type="number"
                v-model="matricula"
            >

        </div>

        <div>

            <label>

                Nome

            </label>

            <input
                type="text"
                v-model="nome"
            >

        </div>

        <div>

            <label>

                Curso

            </label>

            <select
                v-model="curso"
            >

                <option value="">

                    Selecione...

                </option>

                <option
                    v-for="c in cursos"
                    :key="c.id"
                    :value="c.id"
                >

                    {{ c.nome }}

                </option>

            </select>

        </div>

    </div>

    <button
        @click="salvar"
    >

        Salvar Aluno

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
    color:#1e3a8a;
    margin-bottom:25px;

}

.grid{

    display:grid;
    grid-template-columns:repeat(auto-fit,minmax(250px,1fr));
    gap:20px;

}

label{

    display:block;
    margin-bottom:8px;
    font-weight:600;
    color:#444;

}

input,
select{

    width:100%;
    padding:12px;
    border:1px solid #d1d5db;
    border-radius:10px;
    font-size:15px;
    box-sizing:border-box;

}

input:focus,
select:focus{

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
    font-size:15px;

}

button:hover{

    background:#1d4ed8;

}

</style>