def calcular_media(nota1, nota2, nota3):
    return round((nota1 + nota2 + nota3) / 3, 2)


def gerar_relatorio(alunos, notas):

    relatorio_alunos = []

    aprovados = 0
    reprovados = 0
    soma_medias = 0

    melhor_aluno = None
    pior_aluno = None

    cursos = {}

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

                soma_medias += media

                if media >= 6:
                    aprovados += 1
                else:
                    reprovados += 1

                curso = aluno["curso"]

                if curso not in cursos:

                    cursos[curso] = {
                        "nome": curso,
                        "alunos": 0,
                        "soma": 0,
                        "aprovados": 0
                    }

                cursos[curso]["alunos"] += 1
                cursos[curso]["soma"] += media

                if media >= 6:
                    cursos[curso]["aprovados"] += 1

                if melhor_aluno is None or media > melhor_aluno["media"]:

                    melhor_aluno = {
                        "nome": aluno["nome"],
                        "curso": aluno["curso"],
                        "media": media
                    }

                if pior_aluno is None or media < pior_aluno["media"]:

                    pior_aluno = {
                        "nome": aluno["nome"],
                        "curso": aluno["curso"],
                        "media": media
                    }

                break

        relatorio_alunos.append({

            "matricula": aluno["matricula"],

            "nome": aluno["nome"],

            "curso": aluno["curso"],

            "media": media,

            "situacao": situacao

        })

    lista_cursos = []

    for curso in cursos.values():

        lista_cursos.append({

            "nome": curso["nome"],

            "alunos": curso["alunos"],

            "media": round(
                curso["soma"] / curso["alunos"],
                2
            ),

            "aprovados": curso["aprovados"]

        })

    media_geral = 0

    if len(notas) > 0:

        media_geral = round(
            soma_medias / len(notas),
            2
        )

    ranking = sorted(

        [
            a for a in relatorio_alunos
            if a["media"] is not None
        ],

        key=lambda x: x["media"],

        reverse=True

    )

    return {

        "total_alunos": len(alunos),

        "aprovados": aprovados,

        "reprovados": reprovados,

        "media_geral": media_geral,

        "melhor_aluno": melhor_aluno,

        "pior_aluno": pior_aluno,

        "alunos": relatorio_alunos,

        "ranking": ranking,

        "cursos": lista_cursos

    }