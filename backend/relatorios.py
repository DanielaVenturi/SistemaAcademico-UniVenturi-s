def calcular_media(nota1, nota2, nota3):
    return round((nota1 + nota2 + nota3) / 3, 2)


def gerar_relatorio(alunos, notas):

    relatorio_alunos = []

    aprovados = 0
    reprovados = 0
    soma_medias = 0

    melhor_aluno = None
    pior_aluno = None

    for aluno in alunos:

        media = None
        situacao = "Sem notas"

        for nota in notas:

            if nota["aluno_matricula"] == aluno["matricula"]:

                media = calcular_media(
                    nota["nota1"],
                    nota["nota2"],
                    nota["nota3"]
                )

                situacao = (
                    "Aprovado"
                    if media >= 6
                    else "Reprovado"
                )

                if media >= 6:
                    aprovados += 1
                else:
                    reprovados += 1

                soma_medias += media

                if melhor_aluno is None or media > melhor_aluno["media"]:
                    melhor_aluno = {
                        "nome": aluno["nome"],
                        "media": media
                    }

                if pior_aluno is None or media < pior_aluno["media"]:
                    pior_aluno = {
                        "nome": aluno["nome"],
                        "media": media
                    }

                break

        relatorio_alunos.append({

            "matricula": aluno["matricula"],

            "nome": aluno["nome"],

            "media": media,

            "situacao": situacao

        })

    media_geral = 0

    if len(notas) > 0:
        media_geral = round(
            soma_medias / len(notas),
            2
        )

    return {

        "total_alunos": len(alunos),

        "aprovados": aprovados,

        "reprovados": reprovados,

        "media_geral": media_geral,

        "melhor_aluno": melhor_aluno,

        "pior_aluno": pior_aluno,

        "alunos": relatorio_alunos

    }