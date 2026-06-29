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

async function carregarCursos(){

    cursos.value = await listarCursos();

}

async function excluir(id){

    if(!confirm("Deseja realmente excluir este curso?"))
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
defineExpose({

    carregarCursos

});
</script>

<template>

<div class="card">

    <div class="topo">

        <h3>

            Cursos Cadastrados

        </h3>

        <span>

            {{ cursos.length }} registros

        </span>

    </div>

    <table>

        <thead>

            <tr>

                <th>ID</th>

                <th>Nome</th>

                <th class="acoes">

                    Ações

                </th>

            </tr>

        </thead>

        <tbody>

            <tr
                v-for="curso in cursos"
                :key="curso.id"
            >

                <td>

                    {{ curso.id }}

                </td>

                <td>

                    {{ curso.nome }}

                </td>

                <td class="acoes">

                    <button
                        class="editar"
                        @click="abrirModal(curso)"
                    >

                        Editar

                    </button>

                    <button
                        class="excluir"
                        @click="excluir(curso.id)"
                    >

                        Excluir

                    </button>

                </td>

            </tr>

        </tbody>

    </table>

</div>

<EditarCursoModal

    :aberto="modalAberto"

    :curso="cursoSelecionado"

    @fechar="modalAberto=false"

    @atualizado="carregarCursos"

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