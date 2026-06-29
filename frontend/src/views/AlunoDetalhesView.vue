<script setup>

import { ref, onMounted, computed } from "vue";
import { useRoute, useRouter } from "vue-router";

import { buscarPorMatricula } from "../services/alunoService";

import {
    cadastrarNota,
    listarNotasAluno,
    atualizarNota
} from "../services/notaService";

const route = useRoute();
const router = useRouter();

const aluno = ref(null);

const idNota = ref(null);

const nota1 = ref("");
const nota2 = ref("");
const nota3 = ref("");

const editando = ref(false);

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

async function carregarNotas(){

    const notas = await listarNotasAluno(
        route.params.matricula
    );

    if(notas.erro)
        return;

    if(notas.length>0){

        editando.value=true;

        idNota.value=notas[0].id;

        nota1.value=notas[0].nota1;

        nota2.value=notas[0].nota2;

        nota3.value=notas[0].nota3;

    }

}

const media = computed(()=>{

    const n1=Number(nota1.value)||0;
    const n2=Number(nota2.value)||0;
    const n3=Number(nota3.value)||0;

    return ((n1+n2+n3)/3).toFixed(2);

});

const aprovado = computed(()=>{

    return Number(media.value)>=6;

});

async function salvar(){

    const n1 = Number(nota1.value);
    const n2 = Number(nota2.value);
    const n3 = Number(nota3.value);

    if(
        isNaN(n1) ||
        isNaN(n2) ||
        isNaN(n3)
    ){

        alert("Preencha todas as notas.");

        return;

    }

    if(
        n1 < 0 || n1 > 10 ||
        n2 < 0 || n2 > 10 ||
        n3 < 0 || n3 > 10
    ){

        alert("As notas devem estar entre 0 e 10.");

        return;

    }

    const dados = {

        nota1: n1,
        nota2: n2,
        nota3: n3

    };

    if(editando.value){

        await atualizarNota(
            idNota.value,
            dados
        );

        alert("Notas atualizadas com sucesso!");

    }else{

        await cadastrarNota({

            aluno_matricula: aluno.value.matricula,

            ...dados

        });

        alert("Notas cadastradas com sucesso!");

        await carregarNotas();

    }

}
onMounted(async()=>{

    await carregarAluno();

    await carregarNotas();

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

        <div class="cabecalho">

            <div class="avatar">

                {{ aluno.nome.charAt(0).toUpperCase() }}

            </div>

            <div>

                <h1>{{ aluno.nome }}</h1>

                <p>

                    <strong>Matrícula:</strong>

                    {{ aluno.matricula }}

                </p>

                <p>

                    <strong>Curso:</strong>

                    {{ aluno.curso }}

                </p>

            </div>

        </div>

        <hr>

        <h2>

            Lançamento de Notas

        </h2>

        <div class="notas">

            <div>

                <label>N1</label>

                <input
                    type="number"
                    min="0"
                    max="10"
                    step="0.1"
                    v-model="nota1"
                >

            </div>

            <div>

                <label>N2</label>

                <input
                    type="number"
                    min="0"
                    max="10"
                    step="0.1"
                    v-model="nota2"
                >

            </div>

            <div>

                <label>N3</label>

                <input
                    type="number"
                    min="0"
                    max="10"
                    step="0.1"
                    v-model="nota3"
                >

            </div>

        </div>

    <div class="resultado">

    <div class="media-card">

        <h3>Média Final</h3>

        <div class="numero-media">

            {{ media }}

        </div>

        <div
            class="barra"
        >

            <div
                class="preenchimento"
                :style="{ width: (Number(media) * 10) + '%' }"
                :class="aprovado ? 'barra-verde' : 'barra-vermelha'"
            ></div>

        </div>

        <div
            class="situacao"
            :class="aprovado ? 'aprovado' : 'reprovado'"
        >

            {{ aprovado ? " APROVADO" : " REPROVADO" }}

        </div>

    </div>

</div>

        <button
            class="salvar"
            @click="salvar"
        >

            {{ editando ? "Atualizar Notas" : "Salvar Notas" }}

        </button>

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

    padding:10px 18px;

    border:none;

    border-radius:8px;

    background:#2563eb;

    color:white;

    cursor:pointer;

    margin-bottom:25px;

    transition:.2s;

}

.voltar:hover{

    background:#1d4ed8;

}

.card{

    background:white;

    padding:35px;

    border-radius:15px;

    box-shadow:0 4px 15px rgba(0,0,0,.08);

}

.cabecalho{

    display:flex;

    align-items:center;

    gap:25px;

}

.avatar{

    width:90px;

    height:90px;

    border-radius:50%;

    background:#2563eb;

    color:white;

    display:flex;

    justify-content:center;

    align-items:center;

    font-size:40px;

    font-weight:bold;

}
.media-card{

    width:100%;

    background:#f8fafc;

    border-radius:12px;

    padding:25px;

    text-align:center;

    border:1px solid #e5e7eb;

}

.media-card h3{

    margin:0;

    color:#374151;

}

.numero-media{

    font-size:52px;

    font-weight:bold;

    margin:18px 0;

    color:#2563eb;

}

.barra{

    width:100%;

    height:14px;

    background:#ddd;

    border-radius:20px;

    overflow:hidden;

    margin-bottom:18px;

}

.preenchimento{

    height:100%;

    transition:.4s;

}

.barra-verde{

    background:#22c55e;

}

.barra-vermelha{

    background:#ef4444;

}
.cabecalho h1{

    margin:0;

    color:#1e3a8a;

}

.cabecalho p{

    margin:6px 0;

    color:#555;

}

hr{

    margin:30px 0;

    border:none;

    border-top:1px solid #ddd;

}

.notas{

    display:flex;

    gap:20px;

    margin-top:20px;

    margin-bottom:30px;

    flex-wrap:wrap;

}

.notas div{

    flex:1;

    min-width:150px;

}

.notas label{

    display:block;

    margin-bottom:8px;

    font-weight:bold;

}

.notas input{

    width:100%;

    padding:12px;

    border:1px solid #ccc;

    border-radius:8px;

    font-size:16px;

    box-sizing:border-box;

}

.resultado{

    display:flex;

    justify-content:space-between;

    align-items:center;

    margin-top:25px;

    margin-bottom:35px;

    flex-wrap:wrap;

    gap:15px;

}

.media{

    font-size:20px;

    font-weight:bold;

}

.media span{

    color:#2563eb;

    margin-left:10px;

}

.situacao{

    padding:10px 18px;

    border-radius:25px;

    color:white;

    font-weight:bold;

}

.aprovado{

    background:#22c55e;

}

.reprovado{

    background:#ef4444;

}

.salvar{

    width:100%;

    padding:15px;

    border:none;

    border-radius:10px;

    background:#2563eb;

    color:white;

    font-size:17px;

    cursor:pointer;

    transition:.2s;

}

.salvar:hover{

    background:#1d4ed8;

}
</style>