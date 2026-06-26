<script setup>

import { ref, watch, onMounted } from "vue";

import { listarCursos } from "../services/cursoService";
import { atualizarAluno } from "../services/alunoService";

const props = defineProps({

  aberto: Boolean,

  aluno: Object

});

const emit = defineEmits([
  "fechar",
  "atualizado"
]);

const nome = ref("");
const curso_id = ref("");

const cursos = ref([]);

watch(
  () => props.aluno,
  (novoAluno) => {

    if (!novoAluno) return;

    nome.value = novoAluno.nome;

    const curso = cursos.value.find(
      c => c.nome == novoAluno.curso
    );

    curso_id.value = curso ? curso.id : "";

  }
);

onMounted(async () => {

  cursos.value = await listarCursos();

});

async function salvar(){

  await atualizarAluno(

    props.aluno.matricula,

    {

      nome: nome.value,

      curso_id: curso_id.value

    }

  );

  emit("atualizado");

  emit("fechar");

}

</script>

<template>

<div
  v-if="props.aberto"
  class="overlay"
>

  <div class="modal">

    <h2>Editar Aluno</h2>

    <div class="grupo">

      <label>Nome</label>

      <input
        v-model="nome"
      />

    </div>

    <div class="grupo">

      <label>Curso</label>

      <select v-model="curso_id">

        <option
          v-for="curso in cursos"
          :key="curso.id"
          :value="curso.id"
        >
          {{ curso.nome }}
        </option>

      </select>

    </div>

    <div class="botoes">

      <button
        class="cancelar"
        @click="emit('fechar')"
      >
        Cancelar
      </button>

      <button
        class="salvar"
        @click="salvar"
      >
        Salvar
      </button>

    </div>

  </div>

</div>

</template>

<style scoped>

.overlay{

    position:fixed;

    top:0;
    left:0;

    width:100%;
    height:100%;

    background:rgba(0,0,0,.45);

    display:flex;

    justify-content:center;
    align-items:center;

    z-index:999;

}

.modal{

    width:420px;

    background:white;

    border-radius:12px;

    padding:30px;

    box-shadow:0 10px 30px rgba(0,0,0,.25);

}

h2{

    margin-top:0;
    margin-bottom:25px;

    text-align:center;

}

.grupo{

    display:flex;

    flex-direction:column;

    margin-bottom:18px;

}

label{

    font-weight:bold;

    margin-bottom:6px;

}

input,
select{

    padding:10px;

    border:1px solid #ccc;

    border-radius:6px;

    font-size:15px;

}

.botoes{

    display:flex;

    justify-content:flex-end;

    gap:10px;

    margin-top:25px;

}

.salvar{

    background:#4CAF50;

    color:white;

    border:none;

    padding:10px 20px;

    border-radius:6px;

    cursor:pointer;

}

.cancelar{

    background:#e74c3c;

    color:white;

    border:none;

    padding:10px 20px;

    border-radius:6px;

    cursor:pointer;

}
</style>