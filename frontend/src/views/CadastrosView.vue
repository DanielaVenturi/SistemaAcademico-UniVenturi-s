<script setup>

import { ref, onMounted } from "vue";
import { useRoute } from "vue-router";

import CursoForm from "../components/CursoForm.vue";
import TabelaCursos from "../components/TabelaCursos.vue";

import AlunoForm from "../components/AlunoForm.vue";
import TabelaAlunos from "../components/TabelaAlunos.vue";

import ResumoAlunos from "../components/ResumoAlunos.vue";
import ResumoCursos from "../components/ResumoCursos.vue";

const telaAtual = ref("");
const tabelaCursos = ref(null);
const tabelaAlunos = ref(null);

function atualizarTabelaAlunos(){
    tabelaAlunos.value?.carregarAlunos();
}
function atualizarTabelaCursos(){

    tabelaCursos.value?.carregarCursos();

}
const route = useRoute();

onMounted(()=>{

    if(route.query.aba=="cursos"){
        telaAtual.value="cursos";
    }

});

</script>

<template>

<div class="container">

    <h1>Cadastros</h1>

    <p
        v-if="telaAtual==''"
        class="subtitulo"
    >
        Escolha o módulo que deseja gerenciar.
    </p>

    

    <div
        v-if="telaAtual==''"
        class="cards"
    >

        <div class="card">

            

            <h2>

                Alunos

            </h2>

            <p>

                Cadastre, edite e exclua alunos do sistema.

            </p>

            <button
                @click="telaAtual='alunos'"
            >

                Gerenciar Alunos

            </button>

        </div>

        <div class="card">

            

            <h2>

                Cursos

            </h2>

            <p>

                Cadastre e edite todos os cursos.

            </p>

            <button
                @click="telaAtual='cursos'"
            >

                Gerenciar Cursos

            </button>

        </div>

    </div>

    <div
        v-if="telaAtual=='alunos'"
    >

        <button
            class="voltar"
            @click="telaAtual=''"
        >

            ← Voltar

        </button>

        <h2 class="titulo">

            Gerenciamento de Alunos

        </h2>

        <AlunoForm
            @alunoCadastrado="atualizarTabelaAlunos"
        />

        <TabelaAlunos
            ref="tabelaAlunos"
        />

    </div>

    <div
        v-if="telaAtual=='cursos'"
    >

        <button
            class="voltar"
            @click="telaAtual=''"
        >

            ← Voltar

        </button>

        <h2 class="titulo">

            Gerenciamento de Cursos

        </h2>

       <CursoForm
    @cursoCadastrado="atualizarTabelaCursos"
/>

<TabelaCursos
    ref="tabelaCursos"
/>

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
    margin-bottom:10px;

}

.subtitulo{

    text-align:center;
    color:#666;
    margin-bottom:35px;

}

.resumos{

    display:flex;
    gap:20px;
    margin-bottom:35px;
    flex-wrap:wrap;

}

.cards{

    display:grid;
    grid-template-columns:repeat(auto-fit,minmax(320px,1fr));
    gap:30px;

}

.card{

    background:white;
    border-radius:16px;
    padding:35px;
    text-align:center;
    box-shadow:0 5px 15px rgba(0,0,0,.08);
    transition:.25s;

}

.card:hover{

    transform:translateY(-6px);
    box-shadow:0 10px 25px rgba(0,0,0,.12);

}



.card h2{

    color:#1e3a8a;
    margin-bottom:12px;

}

.card p{

    color:#666;
    min-height:45px;

}

button{

    margin-top:20px;
    padding:12px 22px;
    border:none;
    border-radius:10px;
    background:#2563eb;
    color:white;
    cursor:pointer;
    transition:.2s;
    font-size:15px;

}

button:hover{

    background:#1d4ed8;

}

.voltar{

    margin-bottom:25px;

}

.titulo{

    color:#1e3a8a;
    margin-bottom:25px;

}

</style>