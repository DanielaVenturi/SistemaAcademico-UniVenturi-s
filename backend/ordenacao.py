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