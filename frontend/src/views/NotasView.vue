<script setup>
import { ref, onMounted, computed } from "vue";
import { useRoute } from "vue-router";

import { buscarAluno } from "../services/alunoService";

import {
  cadastrarNota,
  listarNotasAluno,
  atualizarNota
} from "../services/notaService";

const route = useRoute();

const aluno = ref(null);

const notaId = ref(null);

const nota1 = ref("");
const nota2 = ref("");
const nota3 = ref("");

const editando = ref(false);

onMounted(async () => {

  const matricula = route.params.matricula;

  aluno.value = await buscarAluno(matricula);

  const notas = await listarNotasAluno(matricula);

  if (!notas.erro && notas.length > 0) {

    editando.value = true;

    notaId.value = notas[0].id;

    nota1.value = notas[0].nota1;

    nota2.value = notas[0].nota2;

    nota3.value = notas[0].nota3;

  }

});

const media = computed(() => {

  const n1 = Number(nota1.value) || 0;
  const n2 = Number(nota2.value) || 0;
  const n3 = Number(nota3.value) || 0;

  return ((n1 + n2 + n3) / 3).toFixed(2);

});

const aprovado = computed(() => {

  return Number(media.value) >= 6;

});

async function salvar(){

  const dados = {

    nota1:Number(nota1.value),
    nota2:Number(nota2.value),
    nota3:Number(nota3.value)

  };

  if(editando.value){

    await atualizarNota(
      notaId.value,
      dados
    );

    alert("Notas atualizadas!");

  }else{

    await cadastrarNota({

      aluno_matricula:aluno.value.matricula,

      ...dados

    });

    alert("Notas cadastradas!");

    editando.value=true;

  }

}
</script>

<template>

  <div class="container">

    <h1>
      📊 Notas
    </h1>

    <button>
      ➕ Lançar Nota
    </button>

    <hr>

    <table>

      <thead>

        <tr>
          <th>Aluno</th>
          <th>N1</th>
          <th>N2</th>
          <th>N3</th>
          <th>Média</th>
        </tr>

      </thead>

    </table>

  </div>

</template>

<style scoped>

.container{
  padding:30px;
}

table{
  margin-top:20px;
}

th{
  padding:10px;
}

</style>