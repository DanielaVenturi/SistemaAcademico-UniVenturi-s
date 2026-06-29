import api from "./api";

export async function buscarNotasAluno(matricula){

    const resposta = await api.get(
        `/notas/aluno/${matricula}`
    );

    return resposta.data;

}

export async function cadastrarNotas(dados){

    const resposta = await api.post(
        "/notas",
        dados
    );

    return resposta.data;

}

export async function atualizarNotas(id,dados){

    const resposta = await api.put(
        `/notas/${id}`,
        dados
    );

    return resposta.data;

}