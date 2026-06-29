const URL = "http://127.0.0.1:5000";

export async function cadastrarNota(dados){

    const resposta = await fetch(`${URL}/notas`,{

        method:"POST",

        headers:{
            "Content-Type":"application/json"
        },

        body:JSON.stringify(dados)

    });

    return await resposta.json();

}

export async function listarNotasAluno(matricula){

    const resposta = await fetch(
        `${URL}/notas/aluno/${matricula}`
    );

    return await resposta.json();

}

export async function atualizarNota(id,dados){

    const resposta = await fetch(

        `${URL}/notas/${id}`,

        {

            method:"PUT",

            headers:{
                "Content-Type":"application/json"
            },

            body:JSON.stringify(dados)

        }

    );

    return await resposta.json();

}

export async function buscarNota(id){

    const resposta = await fetch(
        `${URL}/notas/${id}`
    );

    return await resposta.json();

}