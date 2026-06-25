def ordenar_por_nome(lista):

    lista = lista.copy()
    n = len(lista)

    for i in range(n):
        for j in range(0, n - i - 1):

            if lista[j]["nome"] > lista[j + 1]["nome"]:
                lista[j], lista[j + 1] = lista[j + 1], lista[j]

    return lista


def ordenar_por_matricula(lista):

    lista = lista.copy()
    n = len(lista)

    for i in range(n):
        for j in range(0, n - i - 1):

            if lista[j]["matricula"] > lista[j + 1]["matricula"]:
                lista[j], lista[j + 1] = lista[j + 1], lista[j]

    return lista