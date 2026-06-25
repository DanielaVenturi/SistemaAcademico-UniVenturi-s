import api from "./api";

export async function listarAlunos() {
  const resposta = await api.get("/alunos");
  return resposta.data;
}

export async function cadastrarAluno(aluno) {
  const resposta = await api.post("/alunos", aluno);
  return resposta.data;
}

export async function excluirAluno(matricula) {
  const resposta = await api.delete(`/alunos/${matricula}`);
  return resposta.data;
}

export async function atualizarAluno(matricula, aluno) {
  const resposta = await api.put(
    `/alunos/${matricula}`,
    aluno
  );

  return resposta.data;
}

export async function buscarPorNome(nome) {
  const resposta = await api.get(`/alunos/busca/${nome}`);
  return resposta.data;
}

export async function buscarPorMatricula(matricula) {
  const resposta = await api.get(`/alunos/matricula/${matricula}`);
  return resposta.data;
}

export async function buscarPorCurso(curso) {
  const resposta = await api.get(`/alunos/curso/${curso}`);
  return resposta.data;
}

export async function ordenarPorNome() {
  const resposta = await api.get("/alunos/ordenados");
  return resposta.data;
}

export async function ordenarPorMatricula() {
  const resposta = await api.get("/alunos/ordenados/matricula");
  return resposta.data;
}

export async function ordenarPorCurso() {
  const resposta = await api.get("/alunos/ordenados/curso");
  return resposta.data;
}