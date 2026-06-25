def busca_linear(alunos, termo):

    for aluno in alunos:

        if (
            str(aluno["matricula"]) == str(termo)
            or
            aluno["nome"].lower() == termo.lower()
        ):
            return aluno

    return None