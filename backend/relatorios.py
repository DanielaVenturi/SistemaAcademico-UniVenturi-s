def calcular_media(nota1, nota2, nota3):
    return round((nota1 + nota2 + nota3) / 3, 2)


def gerar_relatorio(alunos, notas):

    total = len(alunos)

    aprovados = 0
    reprovados = 0

    soma_medias = 0

    melhor_aluno = None
    pior_aluno = None

    quantidade_notas = 0

    for nota in notas:

        media = calcular_media(
            nota["nota1"],
            nota["nota2"],
            nota["nota3"]
        )

        quantidade_notas += 1
        soma_medias += media

        aluno = next(

            (
                a for a in alunos
                if a["matricula"] == nota["aluno_matricula"]
            ),

            None

        )

        if media >= 6:
            aprovados += 1
        else:
            reprovados += 1

        if aluno:

            dados = {
                "nome": aluno["nome"],
                "media": media
            }

            if melhor_aluno is None or media > melhor_aluno["media"]:
                melhor_aluno = dados

            if pior_aluno is None or media < pior_aluno["media"]:
                pior_aluno = dados

    media_geral = 0

    if quantidade_notas > 0:
        media_geral = round(
            soma_medias / quantidade_notas,
            2
        )

    return {

        "total_alunos": total,

        "aprovados": aprovados,

        "reprovados": reprovados,

        "media_geral": media_geral,

        "melhor_aluno": melhor_aluno,

        "pior_aluno": pior_aluno

    }