const URL = "http://127.0.0.1:5000";

export async function buscarRelatorio() {

    const resposta = await fetch(`${URL}/relatorio`);

    return await resposta.json();

}