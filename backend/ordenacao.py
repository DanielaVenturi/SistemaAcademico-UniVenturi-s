def bubble_sort_nome(alunos):

    alunos = alunos.copy()

    n = len(alunos)

    for i in range(n):

        for j in range(0, n - i - 1):

            if alunos[j]["nome"] > alunos[j + 1]["nome"]:

                alunos[j], alunos[j + 1] = (
                    alunos[j + 1],
                    alunos[j]
                )

    return alunos

def ordenar_por_nome(lista):

    n = len(lista)

    for i in range(n):

        for j in range(0, n - i - 1):

            if lista[j]["nome"] > lista[j + 1]["nome"]:

                lista[j], lista[j + 1] = (
                    lista[j + 1],
                    lista[j]
                )

    return lista