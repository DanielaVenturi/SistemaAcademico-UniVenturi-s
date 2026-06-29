<script setup>

import { ref, onMounted } from "vue";

import {
  listarAlunos,
  excluirAluno
} from "../services/alunoService";

import EditarAlunoModal from "./EditarAlunoModal.vue";

const alunos = ref([]);

const modalAberto = ref(false);

const alunoSelecionado = ref(null);

async function carregarAlunos(){

    alunos.value = await listarAlunos();

}

async function excluir(matricula){

    if(!confirm("Deseja realmente excluir este aluno?"))
        return;

    await excluirAluno(matricula);

    carregarAlunos();

}

function abrirModal(aluno){

    alunoSelecionado.value = aluno;

    modalAberto.value = true;

}

defineExpose({

    carregarAlunos

});

onMounted(()=>{

    carregarAlunos();

});

</script>

<template>

<div class="card">

    <div class="topo">

        <h3>

            Alunos Cadastrados

        </h3>

        <span>

            {{ alunos.length }} registros

        </span>

    </div>

    <table>

        <thead>

            <tr>

                <th>Matrícula</th>

                <th>Nome</th>

                <th>Curso</th>

                <th class="acoes">

                    Ações

                </th>

            </tr>

        </thead>

        <tbody>

            <tr
                v-for="aluno in alunos"
                :key="aluno.matricula"
            >

                <td>

                    {{ aluno.matricula }}

                </td>

                <td>

                    {{ aluno.nome }}

                </td>

                <td>

                    {{ aluno.curso }}

                </td>

                <td class="acoes">

                    <button
                        class="editar"
                        @click="abrirModal(aluno)"
                    >

                        Editar

                    </button>

                    <button
                        class="excluir"
                        @click="excluir(aluno.matricula)"
                    >

                        Excluir

                    </button>

                </td>

            </tr>

        </tbody>

    </table>

</div>

<EditarAlunoModal

    :aberto="modalAberto"

    :aluno="alunoSelecionado"

    @fechar="modalAberto=false"

    @atualizado="carregarAlunos"

/>

</template>

<style scoped>

.card{

    background:white;
    padding:30px;
    border-radius:14px;
    box-shadow:0 4px 15px rgba(0,0,0,.08);

}

.topo{

    display:flex;
    justify-content:space-between;
    align-items:center;
    margin-bottom:20px;

}

.topo h3{

    margin:0;
    color:#1e3a8a;

}

.topo span{

    background:#eff6ff;
    color:#2563eb;
    padding:6px 14px;
    border-radius:30px;
    font-size:14px;
    font-weight:600;

}

table{

    width:100%;
    border-collapse:collapse;

}

thead{

    background:#2563eb;
    color:white;

}

th{

    padding:15px;
    text-align:left;

}

td{

    padding:15px;
    border-bottom:1px solid #ececec;

}

tbody tr{

    transition:.2s;

}

tbody tr:hover{

    background:#f8fbff;

}

.acoes{

    text-align:center;
    white-space:nowrap;

}

button{

    border:none;
    border-radius:8px;
    padding:9px 14px;
    cursor:pointer;
    color:white;
    font-size:14px;
    transition:.2s;

}

.editar{

    background:#2563eb;
    margin-right:8px;

}

.editar:hover{

    background:#1d4ed8;

}

.excluir{

    background:#dc2626;

}

.excluir:hover{

    background:#b91c1c;

}

</style>