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

<div
    class="container"
    v-if="relatorio"
>


   

    <div class="cards">

        <div class="card azul">
            <h2>{{ relatorio.total_alunos }}</h2>
            <p>Alunos</p>
        </div>

        <div class="card verde">
            <h2>{{ relatorio.aprovados }}</h2>
            <p>Aprovados</p>
        </div>

        <div class="card vermelho">
            <h2>{{ relatorio.reprovados }}</h2>
            <p>Reprovados</p>
        </div>

        <div class="card roxo">
            <h2>{{ relatorio.media_geral }}</h2>
            <p>Média Geral</p>
        </div>

    </div>


    <div class="destaques">

        <div
            class="box melhor"
            v-if="relatorio.melhor_aluno"
        >

            <h2>Melhor Aluno</h2>

            <h3>{{ relatorio.melhor_aluno.nome }}</h3>

            <p>

                <strong>Curso:</strong>

                {{ relatorio.melhor_aluno.curso }}

            </p>

            <p>

                Média:

                <strong>{{ relatorio.melhor_aluno.media }}</strong>

            </p>

        </div>

        <div
            class="box pior"
            v-if="relatorio.pior_aluno"
        >

            <h2>Pior Aluno</h2>

            <h3>{{ relatorio.pior_aluno.nome }}</h3>

            <p>

                <strong>Curso:</strong>

                {{ relatorio.pior_aluno.curso }}

            </p>

            <p>

                Média:

                <strong>{{ relatorio.pior_aluno.media }}</strong>

            </p>

        </div>

    </div>


    <div class="secao">

        <h2>Ranking de Médias</h2>

        <table>

            <thead>

                <tr>

                    <th>#</th>

                    <th>Aluno</th>

                    <th>Curso</th>

                    <th>Média</th>

                </tr>

            </thead>

            <tbody>

                <tr
                    v-for="(aluno,index) in relatorio.ranking"
                    :key="aluno.matricula"
                >

                    <td>{{ index + 1 }}</td>

                    <td>{{ aluno.nome }}</td>

                    <td>{{ aluno.curso }}</td>

                    <td>{{ aluno.media }}</td>

                </tr>

            </tbody>

        </table>

    </div>

    

    <div class="secao">

        <h2>Desempenho por Curso</h2>

        <table>

            <thead>

                <tr>

                    <th>Curso</th>

                    <th>Alunos</th>

                    <th>Média</th>

                    <th>Aprovados</th>

                </tr>

            </thead>

            <tbody>

                <tr
                    v-for="curso in relatorio.cursos"
                    :key="curso.nome"
                >

                    <td>{{ curso.nome }}</td>

                    <td>{{ curso.alunos }}</td>

                    <td>{{ curso.media }}</td>

                    <td>{{ curso.aprovados }}</td>

                </tr>

            </tbody>

        </table>

    </div>

    <!-- Todos os alunos -->

    <div class="secao">

        <h2>Lista Geral</h2>

        <table>

            <thead>

                <tr>

                    <th>Matrícula</th>

                    <th>Nome</th>

                    <th>Curso</th>

                    <th>Média</th>

                    <th>Situação</th>

                </tr>

            </thead>

            <tbody>

                <tr
                    v-for="aluno in relatorio.alunos"
                    :key="aluno.matricula"
                >

                    <td>{{ aluno.matricula }}</td>

                    <td>{{ aluno.nome }}</td>

                    <td>{{ aluno.curso }}</td>

                    <td>

                        {{ aluno.media ?? "-" }}

                    </td>

                    <td>

                        <span
                            :class="[
                                'badge',
                                aluno.situacao=='Aprovado'
                                    ? 'verde'
                                    : aluno.situacao=='Reprovado'
                                    ? 'vermelho'
                                    : 'cinza'
                            ]"
                        >

                            {{ aluno.situacao }}

                        </span>

                    </td>

                </tr>

            </tbody>

        </table>

    </div>

</div>

</template>

<style scoped>

.container{
    max-width: 1200px;
    margin: auto;
    padding: 35px;
}

h1{
    text-align: center;
    color: #1e3a8a;
    margin-bottom: 35px;
}

.cards{
    display: grid;
    grid-template-columns: repeat(auto-fit,minmax(220px,1fr));
    gap: 20px;
    margin-bottom: 35px;
}

.card{
    color: white;
    border-radius: 14px;
    padding: 25px;
    text-align: center;
    box-shadow: 0 5px 15px rgba(0,0,0,.12);
}

.card h2{
    margin: 0;
    font-size: 38px;
}

.card p{
    margin-top: 10px;
    font-size: 17px;
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
    grid-template-columns:repeat(auto-fit,minmax(350px,1fr));
    gap:20px;
    margin-bottom:35px;
}

.box{
    background:white;
    padding:25px;
    border-radius:14px;
    box-shadow:0 5px 15px rgba(0,0,0,.08);
}

.melhor{
    border-left:8px solid #22c55e;
}

.pior{
    border-left:8px solid #ef4444;
}

.box h2{
    margin-top:0;
}

.box h3{
    color:#1e3a8a;
    margin-bottom:10px;
}

.secao{
    margin-top:35px;
}

.secao h2{
    margin-bottom:18px;
    color:#1e3a8a;
}

table{
    width:100%;
    border-collapse:collapse;
    background:white;
    border-radius:12px;
    overflow:hidden;
    box-shadow:0 4px 12px rgba(0,0,0,.08);
}

thead{
    background:#2563eb;
    color:white;
}

th{
    padding:14px;
    text-align:left;
}

td{
    padding:14px;
    border-bottom:1px solid #eee;
}

tbody tr:hover{
    background:#f8fbff;
}

.badge{
    padding:6px 14px;
    border-radius:25px;
    color:white;
    font-weight:bold;
    display:inline-block;
}

.badge.verde{
    background:#22c55e;
}

.badge.vermelho{
    background:#ef4444;
}

.badge.cinza{
    background:#9ca3af;
}

@media(max-width:700px){

    .container{
        padding:20px;
    }

    table{
        display:block;
        overflow-x:auto;
    }

}

</style>