def busca_por_nome(lista_alunos, nome_procurado):

    resultado = []

    for aluno in lista_alunos:

        if nome_procurado.lower() in aluno["nome"].lower():

            resultado.append(aluno)

    return resultado