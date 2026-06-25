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
  const resposta = await api.delete(
    `/alunos/${matricula}`
  );

  return resposta.data;
}