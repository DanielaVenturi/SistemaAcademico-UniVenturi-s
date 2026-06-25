def busca_linear(alunos, termo):

    for aluno in alunos:

        if (
            str(aluno["matricula"]) == str(termo)
            or
            aluno["nome"].lower() == termo.lower()
        ):
            return aluno

    return None

def busca_por_nome(lista_alunos, nome_procurado):

    resultado = []

    for aluno in lista_alunos:

        if nome_procurado.lower() in aluno["nome"].lower():

            resultado.append(aluno)

    return resultado

def busca_por_matricula(lista_alunos, matricula):

    for aluno in lista_alunos:

        if aluno["matricula"] == matricula:

            return aluno

    return None