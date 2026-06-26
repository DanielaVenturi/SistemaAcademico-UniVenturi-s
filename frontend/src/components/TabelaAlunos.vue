<script setup>

import { ref, onMounted } from "vue";

import {
  listarAlunos,
  excluirAluno,
  atualizarAluno
} from "../services/alunoService";

import { listarCursos } from "../services/cursoService";
import EditarAlunoModal from "./EditarAlunoModal.vue";

const modalAberto = ref(false);
const alunoSelecionado = ref(null);
const alunos = ref([]);
const cursos = ref([]);
const editando = ref(null);
const nome = ref("");
const curso_id = ref("");

async function carregarAlunos() {
  alunos.value = await listarAlunos();
}

async function carregarCursos() {
  cursos.value = await listarCursos();
}

async function excluir(matricula) {

  if (!confirm("Deseja excluir este aluno?"))
    return;

  await excluirAluno(matricula);

  carregarAlunos();
}

function editar(aluno) {

  editando.value = aluno.matricula;

  nome.value = aluno.nome;

  const curso = cursos.value.find(
    c => c.nome == aluno.curso
  );

  curso_id.value = curso ? curso.id : "";

}

async function salvarEdicao(matricula) {

  await atualizarAluno(
    matricula,
    {
      nome: nome.value,
      curso_id: curso_id.value
    }
  );

  editando.value = null;

  carregarAlunos();

}
function abrirModal(aluno){

  alunoSelecionado.value = aluno;

  modalAberto.value = true;

}
onMounted(() => {

  carregarAlunos();

  carregarCursos();

});

</script>

<template>

<h2>Lista de Alunos</h2>

<table border="1">

<thead>

<tr>

<th>Matrícula</th>
<th>Nome</th>
<th>Curso</th>
<th>Ações</th>

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

<input
v-if="editando==aluno.matricula"
v-model="nome"
/>

<span
v-else
>

{{ aluno.nome }}

</span>

</td>

<td>

<select
v-if="editando==aluno.matricula"
v-model="curso_id"
>

<option
v-for="curso in cursos"
:key="curso.id"
:value="curso.id"
>

{{ curso.nome }}

</option>

</select>

<span
v-else
>

{{ aluno.curso }}

</span>

</td>

<td>

<button
@click="abrirModal(aluno)"
>

Editar

</button>



<button
@click="excluir(aluno.matricula)"
>

Excluir

</button>

</td>

</tr>

</tbody>

</table>
<EditarAlunoModal

  :aberto="modalAberto"

  :aluno="alunoSelecionado"

  @fechar="modalAberto=false"

  @atualizado="carregarAlunos"

/>
</template>