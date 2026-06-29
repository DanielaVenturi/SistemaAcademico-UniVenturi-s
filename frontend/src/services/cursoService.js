import api from "./api";

export async function listarCursos() {
  const resposta = await api.get("/cursos");
  return resposta.data;
}

export async function cadastrarCurso(dados){

    const resposta = await api.post(
        "/cursos",
        dados
    );

    return resposta.data;

}

export async function atualizarCurso(id, dados){

    const resposta = await api.put(

        `/cursos/${id}`,

        dados

    );

    return resposta.data;

}

export async function excluirCurso(id) {
  const resposta = await api.delete(`/cursos/${id}`);
  return resposta.data;
}