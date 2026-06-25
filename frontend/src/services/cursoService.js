import api from "./api";

export async function listarCursos() {
  const resposta = await api.get("/cursos");
  return resposta.data;
}

export async function cadastrarCurso(nome) {
  const resposta = await api.post("/cursos", {
    nome
  });

  return resposta.data;
}

export async function excluirCurso(id) {
  const resposta = await api.delete(`/cursos/${id}`);
  return resposta.data;
}