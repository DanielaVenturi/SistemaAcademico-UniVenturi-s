# Sistema Acadêmico UniVenturi

**Aluna:** Daniela Venturi  
**Disciplina:** Engenharia de Software  
**Turma:** 144-2An

---

# Sobre o Projeto

O Sistema Acadêmico UniVenturi foi desenvolvido como projeto da disciplina de Algoritmos e Lógica de Programação.

O objetivo principal era desenvolver um sistema acadêmico utilizando **Python**, colocando em prática os conteúdos estudados durante a disciplina, como:

- Listas
- Funções
- Busca
- Ordenação
- Matrizes
- Relatórios

Embora o foco do trabalho fosse o back-end em Python, também foi desenvolvido um front-end utilizando Vue.js para tornar o sistema mais intuitivo e agradável de utilizar.

---

# Tecnologias Utilizadas

## Back-end

- Python
- Flask
- SQLite

## Front-end

- Vue.js
- Axios
- Vite

---

# Como executar o projeto

## 1° Passo

Clone o repositório para o computador.

Depois abra o projeto no Visual Studio Code.

---

## 2° Passo

Abra um terminal e entre na pasta do back-end.

```bash
cd backend
```
---

## 3° Passo

Ative o ambiente virtual.

```powershell
python -m venv venv


.\venv\Scripts\Activate.ps1
```

## 4° Passo

Execute o servidor Flask.

```bash
python app.py
```

Esse comando inicia o servidor responsável pelo funcionamento da API do sistema.

**Não feche este terminal.**

---

## 5° Passo

Abra um **novo terminal**, mantendo o primeiro aberto.

Entre na pasta do front-end.

```bash
cd frontend
```

---

## 6° Passo

Instale as dependências do projeto.

```bash
npm install
```
## 7° Passo

Execute o front-end.

```bash
npm run dev
```

Após alguns segundos será exibida uma URL semelhante a:

```
http://localhost:5173
```

Copie essa URL e abra no navegador.

O sistema estará funcionando.

---

# Objetivo do Sistema

O UniVenturi é um pequeno sistema de gestão acadêmica.

Ele permite:

- Cadastro de cursos;
- Cadastro de alunos;
- Consulta de alunos;
- Busca por nome;
- Busca por matrícula;
- Busca por curso;
- Ordenação dos registros;
- Cadastro de notas;
- Atualização de notas;
- Cálculo automático da média;
- Situação do aluno;
- Relatórios gerais;
- Ranking de desempenho.

---

# Organização do Back-end

O projeto foi dividido em arquivos para facilitar sua organização.

## app.py


É responsável pelas rotas da API, comunicação com o banco de dados e integração entre todos os módulos.

---

## database.py

Responsável pela criação das tabelas e conexão com o banco SQLite.

---

# busca.py

Nesse arquivo foram implementados os algoritmos de busca estudados durante a disciplina.

As funções trabalham sobre a lista de alunos cadastrados e permitem localizar informações de diferentes maneiras.

---

## Busca Linear

```python
def busca_linear(alunos, termo):

    for aluno in alunos:

        if (
            str(aluno["matricula"]) == str(termo)
            or
            aluno["nome"].lower() == termo.lower()
        ):
            return aluno

    return None
```

Essa função percorre a lista de alunos do início ao fim.

Durante o percurso ela verifica se a matrícula ou o nome do aluno é igual ao termo informado.

Se encontrar o aluno, a função retorna imediatamente aquele registro.

Caso percorra toda a lista sem encontrar nenhum resultado, retorna `None`.

Essa implementação representa o algoritmo clássico de **Busca Linear**, visto em sala de aula.

---

## Busca por Nome

```python
def busca_por_nome(lista_alunos, nome_procurado):

    resultado = []

    for aluno in lista_alunos:

        if nome_procurado.lower() in aluno["nome"].lower():

            resultado.append(aluno)

    return resultado
```

Essa função também percorre toda a lista de alunos.

Ao invés de procurar apenas um nome exatamente igual, ela verifica se o texto pesquisado faz parte do nome do aluno.

Todos os alunos encontrados são adicionados em uma lista chamada `resultado`.

Ao final da busca, essa lista é retornada.

Isso permite localizar vários alunos utilizando apenas parte do nome.

---

## Busca por Matrícula

```python
def busca_por_matricula(lista_alunos, matricula):

    for aluno in lista_alunos:

        if aluno["matricula"] == matricula:

            return aluno

    return None
```

Essa função percorre toda a lista verificando a matrícula de cada aluno.

Assim que encontra a matrícula informada, retorna imediatamente aquele aluno.

Caso não exista nenhum aluno com essa matrícula, retorna `None`.

---

## Busca por Curso

```python
def busca_por_curso(lista_alunos, curso_procurado):

    resultado = []

    for aluno in lista_alunos:

        if (
            aluno["curso"]
            and
            curso_procurado.lower()
            in aluno["curso"].lower()
        ):
            resultado.append(aluno)

    return resultado
```

Essa função percorre todos os alunos cadastrados.

Sempre que o curso do aluno contém o texto pesquisado, esse aluno é adicionado à lista de resultados.

Ao final, a função retorna todos os alunos pertencentes ao curso pesquisado.

Esse algoritmo permite encontrar rapidamente todos os alunos de um determinado curso.

---

# ordenacao.py

Nesse arquivo foi implementado o algoritmo **Bubble Sort**, conteúdo estudado durante a disciplina.

O Bubble Sort funciona comparando dois elementos vizinhos da lista.

Sempre que eles estão fora da ordem correta, ocorre uma troca de posição.

Esse processo é repetido diversas vezes até que toda a lista esteja ordenada.

---

## Ordenação por Nome

```python
def ordenar_por_nome(lista):

    lista = lista.copy()
    n = len(lista)

    for i in range(n):
        for j in range(0, n - i - 1):

            if lista[j]["nome"] > lista[j + 1]["nome"]:
                lista[j], lista[j + 1] = lista[j + 1], lista[j]

    return lista
```

Essa função organiza todos os alunos em ordem alfabética crescente.

Ela utiliza o algoritmo Bubble Sort para comparar os nomes dos alunos e realizar as trocas necessárias até que todos estejam ordenados corretamente.

---

## Ordenação por Matrícula

```python
def ordenar_por_matricula(lista):

    lista = lista.copy()
    n = len(lista)

    for i in range(n):
        for j in range(0, n - i - 1):

            if lista[j]["matricula"] > lista[j + 1]["matricula"]:
                lista[j], lista[j + 1] = lista[j + 1], lista[j]

    return lista
```

Essa função utiliza o Bubble Sort para organizar os alunos pela matrícula.

Ao final da execução, os alunos ficam ordenados da menor matrícula para a maior.

---

## Ordenação por Curso

```python
def ordenar_por_curso(lista):

    lista = lista.copy()

    n = len(lista)

    for i in range(n):

        for j in range(0, n - i - 1):

            curso_atual = lista[j]["curso"] or ""
            curso_proximo = lista[j + 1]["curso"] or ""

            if curso_atual > curso_proximo:

                lista[j], lista[j + 1] = (
                    lista[j + 1],
                    lista[j]
                )

    return lista
```

Essa função organiza os alunos em ordem alfabética de acordo com o curso.

Durante a comparação é feita uma verificação para evitar problemas caso algum aluno não possua curso cadastrado.

Assim como nas outras funções, o algoritmo utilizado é o Bubble Sort.

---

# relatorios.py

Esse arquivo é responsável por gerar todas as estatísticas do sistema acadêmico.

A partir das listas de alunos e notas cadastradas, ele calcula médias, identifica alunos aprovados e reprovados, gera rankings e produz informações gerais sobre cada curso.

---

## Cálculo da Média

```python
def calcular_media(nota1, nota2, nota3):
    return round((nota1 + nota2 + nota3) / 3, 2)
```

Essa função recebe as três notas de um aluno.

Em seguida calcula a média aritmética simples.

O resultado é arredondado para duas casas decimais utilizando a função `round()`.

Essa função é utilizada em todo o sistema sempre que é necessário calcular a média de um aluno.

---

## Geração do Relatório

```python
def gerar_relatorio(alunos, notas):
```

Essa função recebe duas listas:

- Lista de alunos;
- Lista de notas.

A partir dessas informações ela percorre todos os alunos cadastrados e procura suas respectivas notas.

Quando encontra as notas de um aluno:

- calcula sua média;
- determina se foi aprovado ou reprovado;
- contabiliza os totais gerais;
- atualiza as estatísticas do curso;
- verifica se aquele aluno possui a maior ou a menor média.

Durante esse processamento também são calculadas diversas informações importantes para o sistema.

Entre elas:

- quantidade total de alunos;
- quantidade de aprovados;
- quantidade de reprovados;
- média geral da instituição;
- melhor aluno;
- pior aluno;
- ranking geral dos alunos;
- estatísticas de cada curso.

Ao final, todas essas informações são organizadas em um único dicionário e retornadas para serem exibidas na tela de relatórios do sistema.

Dessa forma, todo o processamento dos dados acontece no backend, deixando o frontend responsável apenas por apresentar as informações ao usuário.

----

# Estruturas de Dados Utilizadas

Durante o desenvolvimento foram utilizados diversos conceitos estudados durante a disciplina.

## Listas

As listas armazenam:

- alunos;
- cursos;
- notas;
- ranking;
- resultados das buscas;
- relatórios.

---


## Matrizes

Durante a disciplina foi estudado o conceito de matrizes como estruturas bidimensionais compostas por linhas e colunas.

Embora o sistema utilize banco de dados SQLite para armazenar as informações de forma permanente, esse conceito continua presente durante o processamento dos dados.

Quando é executado:

```python
cursor.fetchall()
```

o SQLite retorna uma coleção de registros organizada em linhas e colunas.

Exemplo:

```python
[
    (1, "Daniela", "Engenharia de Software"),
    (2, "Ana", "Administração"),
    (3, "Carlos", "Informática")
]
```

Cada linha representa um registro.

Cada coluna representa um atributo desse registro.

Essa estrutura corresponde ao conceito de matriz bidimensional estudado durante a disciplina.

Após a leitura desses dados, eles são convertidos para listas de dicionários, facilitando a manipulação das informações pelo restante da aplicação.
---
# Requisitos da Disciplina

Durante o desenvolvimento do projeto foram contemplados todos os principais conteúdos apresentados na disciplina.

| Requisito | Aplicação no Projeto |
|-----------|----------------------|
| Listas | Cadastro e manipulação de alunos, cursos, notas e relatórios |
| Matrizes | Estrutura tabular retornada pelo SQLite através do `fetchall()` |
| Funções | Organização modular em diversos arquivos Python |
| Busca Linear | Implementada em `busca.py` |
| Ordenação (Bubble Sort) | Implementada em `ordenacao.py` |
| Relatórios | Implementados em `relatorios.py` |
| Modularização | Separação da aplicação em arquivos específicos |
| Banco de Dados | SQLite |
| Interface | Desenvolvida em Vue.js como complemento ao backend |

# Considerações Finais

O desenvolvimento do Sistema Acadêmico UniVenturi permitiu aplicar, de forma prática, os principais conceitos estudados na disciplina de Algoritmos e Lógica de Programação. Durante o projeto foram utilizados listas, matrizes (na representação tabular dos dados), funções, modularização, algoritmos de busca linear, algoritmos de ordenação (Bubble Sort), cálculo de médias, geração de relatórios e manipulação de banco de dados com SQLite.

Embora o foco da disciplina fosse o desenvolvimento do backend em Python, também foi desenvolvida uma interface em Vue.js para proporcionar uma melhor experiência ao usuário e demonstrar a integração entre frontend e backend por meio de uma API REST construída com Flask.

Como resultado, foi desenvolvido um sistema acadêmico completo, organizado e funcional, capaz de gerenciar cursos, alunos e notas, além de realizar buscas, ordenações, consultas e gerar relatórios de desempenho. O projeto representa a aplicação dos conhecimentos adquiridos ao longo da disciplina e contribuiu para o desenvolvimento de boas práticas de programação, organização de código e desenvolvimento de software.
