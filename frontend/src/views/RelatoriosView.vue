<script setup>

import { ref, onMounted } from "vue";

import { buscarRelatorio } from "../services/relatorioService";

const relatorio = ref(null);

async function carregarRelatorio(){

    relatorio.value = await buscarRelatorio();

}

onMounted(() => {

    carregarRelatorio();

});

</script>

<template>

<div class="container">

    <h1>📊 Relatórios</h1>

    <div
        v-if="relatorio"
    >

        <div class="cards">

            <div class="card azul">

                <h3>Total de Alunos</h3>

                <h2>{{ relatorio.total_alunos }}</h2>

            </div>

            <div class="card verde">

                <h3>Aprovados</h3>

                <h2>{{ relatorio.aprovados }}</h2>

            </div>

            <div class="card vermelho">

                <h3>Reprovados</h3>

                <h2>{{ relatorio.reprovados }}</h2>

            </div>

            <div class="card roxo">

                <h3>Média Geral</h3>

                <h2>{{ relatorio.media_geral }}</h2>

            </div>

        </div>

        <div class="destaques">

            <div class="box">

                <h2>🏆 Melhor Aluno</h2>

                <p>

                    <strong>

                        {{ relatorio.melhor_aluno?.nome || "-" }}

                    </strong>

                </p>

                <h1>

                    {{ relatorio.melhor_aluno?.media || "-" }}

                </h1>

            </div>

            <div class="box">

                <h2>📉 Pior Aluno</h2>

                <p>

                    <strong>

                        {{ relatorio.pior_aluno?.nome || "-" }}

                    </strong>

                </p>

                <h1>

                    {{ relatorio.pior_aluno?.media || "-" }}

                </h1>

            </div>

        </div>

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

    text-align:center;

    color:#1e3a8a;

    margin-bottom:35px;

}

.cards{

    display:grid;

    grid-template-columns:repeat(auto-fit,minmax(220px,1fr));

    gap:20px;

}

.card{

    padding:25px;

    border-radius:15px;

    color:white;

    text-align:center;

    box-shadow:0 3px 12px rgba(0,0,0,.15);

}

.card h3{

    margin:0;

    font-weight:500;

}

.card h2{

    font-size:38px;

    margin-top:20px;

}

.azul{

    background:#2563eb;

}

.verde{

    background:#16a34a;

}

.vermelho{

    background:#dc2626;

}

.roxo{

    background:#7c3aed;

}

.destaques{

    display:grid;

    grid-template-columns:1fr 1fr;

    gap:25px;

    margin-top:35px;

}

.box{

    background:white;

    border-radius:15px;

    padding:30px;

    text-align:center;

    box-shadow:0 3px 12px rgba(0,0,0,.08);

}

.box h1{

    color:#2563eb;

    margin-top:15px;

}

@media(max-width:700px){

    .destaques{

        grid-template-columns:1fr;

    }

}

</style>