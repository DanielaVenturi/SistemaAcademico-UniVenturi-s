from flask import Flask, request
from flask_cors import CORS

from database import criar_tabelas, conectar
from busca import (
    busca_por_nome,
    busca_por_matricula,
    busca_por_curso
)
from ordenacao import (
    ordenar_por_nome,
    ordenar_por_matricula,
    ordenar_por_curso
)
from relatorios import (
    calcular_media,
    gerar_relatorio
)

from datetime import datetime
app = Flask(__name__)
CORS(app)

criar_tabelas()

print("APP ATUALIZADO CARREGADO")


@app.route("/")
def home():
    return {"mensagem": "Sistema Acadêmico Online"}


@app.route("/cursos", methods=["POST"])
def cadastrar_curso():

    dados = request.json

    conn = conectar()
    cursor = conn.cursor()

    cursor.execute("""
        INSERT INTO cursos (nome)
        VALUES (?)
    """, (dados["nome"],))

    conn.commit()
    conn.close()

    return {"mensagem": "Curso cadastrado com sucesso"}

@app.route("/cursos", methods=["GET"])
def listar_cursos():

    conn = conectar()
    cursor = conn.cursor()

    cursor.execute("SELECT id, nome FROM cursos")
    dados = cursor.fetchall()
    conn.close()

    cursos = []

    for c in dados:
        cursos.append({
            "id": c[0],
            "nome": c[1]
        })

    return cursos

@app.route("/alunos", methods=["POST"])
def cadastrar_aluno():

    dados = request.json

    conn = conectar()
    cursor = conn.cursor()

    cursor.execute("""
        INSERT INTO alunos (matricula, nome, curso_id)
        VALUES (?, ?, ?)
    """, (
        dados["matricula"],
        dados["nome"],
        dados["curso_id"]
    ))

    conn.commit()
    conn.close()

    return {"mensagem": "Aluno cadastrado com sucesso"}

@app.route("/cursos/<int:id>", methods=["DELETE"])
def excluir_curso(id):

    conn = conectar()
    cursor = conn.cursor()

    cursor.execute("""
        DELETE FROM cursos
        WHERE id = ?
    """, (id,))

    conn.commit()
    conn.close()

    return {
        "mensagem": "Curso excluído com sucesso"
    }

@app.route("/cursos/<int:id>", methods=["PUT"])
def atualizar_curso(id):

    dados = request.json

    conn = conectar()
    cursor = conn.cursor()

    cursor.execute("""
        UPDATE cursos
        SET nome = ?
        WHERE id = ?
    """, (
        dados["nome"],
        id
    ))

    conn.commit()
    conn.close()

    return {
        "mensagem": "Curso atualizado com sucesso"
    }

@app.route("/alunos", methods=["GET"])
def listar_alunos():

    conn = conectar()
    cursor = conn.cursor()

    cursor.execute("""
        SELECT a.matricula, a.nome, c.nome
        FROM alunos a
        LEFT JOIN cursos c ON a.curso_id = c.id
    """)

    dados = cursor.fetchall()
    conn.close()

    alunos = []

    for a in dados:
        alunos.append({
            "matricula": a[0],
            "nome": a[1],
            "curso": a[2]
        })

    return alunos

@app.route("/alunos/<int:matricula>", methods=["GET"])
def buscar_aluno(matricula):

    conn = conectar()
    cursor = conn.cursor()

    cursor.execute("""
        SELECT
            a.matricula,
            a.nome,
            c.id,
            c.nome
        FROM alunos a
        LEFT JOIN cursos c
        ON a.curso_id = c.id
        WHERE a.matricula = ?
    """, (matricula,))

    aluno = cursor.fetchone()

    conn.close()

    if aluno is None:

        return {
            "erro": "Aluno não encontrado"
        }, 404

    return {
        "matricula": aluno[0],
        "nome": aluno[1],
        "curso_id": aluno[2],
        "curso": aluno[3]
    }

@app.route("/alunos/<int:matricula>", methods=["PUT"])
def atualizar_aluno(matricula):

    dados = request.json

    conn = conectar()
    cursor = conn.cursor()

    cursor.execute("""
        UPDATE alunos
        SET nome = ?, curso_id = ?
        WHERE matricula = ?
    """, (
        dados["nome"],
        dados["curso_id"],
        matricula
    ))

    conn.commit()
    conn.close()

    return {"mensagem": "Aluno atualizado com sucesso"}


@app.route("/alunos/<int:matricula>", methods=["DELETE"])
def deletar_aluno(matricula):

    conn = conectar()
    cursor = conn.cursor()

    cursor.execute("""
        DELETE FROM alunos
        WHERE matricula = ?
    """, (matricula,))

    conn.commit()
    conn.close()

    return {"mensagem": "Aluno deletado com sucesso"}


@app.route("/alunos/busca/<nome>")
def buscar_por_nome(nome):

    conn = conectar()
    cursor = conn.cursor()

    cursor.execute("""
        SELECT a.matricula, a.nome, c.nome
        FROM alunos a
        LEFT JOIN cursos c
        ON a.curso_id = c.id
    """)

    dados = cursor.fetchall()
    conn.close()

    alunos = []

    for a in dados:
        alunos.append({
            "matricula": a[0],
            "nome": a[1],
            "curso": a[2]
        })

    return busca_por_nome(alunos, nome)

@app.route("/alunos/curso/<curso>")
def buscar_por_curso(curso):

    conn = conectar()
    cursor = conn.cursor()

    cursor.execute("""
        SELECT a.matricula, a.nome, c.nome
        FROM alunos a
        LEFT JOIN cursos c
        ON a.curso_id = c.id
    """)

    dados = cursor.fetchall()

    conn.close()

    alunos = []

    for a in dados:
        alunos.append({
            "matricula": a[0],
            "nome": a[1],
            "curso": a[2]
        })

    return busca_por_curso(
        alunos,
        curso
    )

@app.route("/alunos/matricula/<int:matricula>")
def buscar_por_matricula(matricula):

    conn = conectar()
    cursor = conn.cursor()

    cursor.execute("""
        SELECT a.matricula, a.nome, c.nome
        FROM alunos a
        LEFT JOIN cursos c
        ON a.curso_id = c.id
    """)

    dados = cursor.fetchall()
    conn.close()

    alunos = []

    for a in dados:
        alunos.append({
            "matricula": a[0],
            "nome": a[1],
            "curso": a[2]
        })

    resultado = busca_por_matricula(
        alunos,
        matricula
    )

    if resultado:
        return resultado

    return {
        "erro": "Aluno não encontrado"
    }, 404


@app.route("/alunos/ordenados")
def alunos_ordenados():

    conn = conectar()
    cursor = conn.cursor()

    cursor.execute("""
        SELECT a.matricula, a.nome, c.nome
        FROM alunos a
        LEFT JOIN cursos c
        ON a.curso_id = c.id
    """)

    dados = cursor.fetchall()
    conn.close()

    alunos = []

    for a in dados:
        alunos.append({
            "matricula": a[0],
            "nome": a[1],
            "curso": a[2]
        })

    return ordenar_por_nome(alunos)

@app.route("/alunos/ordenados/matricula")
def alunos_ordenados_matricula():

    conn = conectar()
    cursor = conn.cursor()

    cursor.execute("""
        SELECT a.matricula, a.nome, c.nome
        FROM alunos a
        LEFT JOIN cursos c
        ON a.curso_id = c.id
    """)

    dados = cursor.fetchall()

    conn.close()

    alunos = []

    for a in dados:
        alunos.append({
            "matricula": a[0],
            "nome": a[1],
            "curso": a[2]
        })

    return ordenar_por_matricula(alunos)

@app.route("/alunos/ordenados/curso")
def alunos_ordenados_curso():

    conn = conectar()
    cursor = conn.cursor()

    cursor.execute("""
        SELECT a.matricula, a.nome, c.nome
        FROM alunos a
        LEFT JOIN cursos c
        ON a.curso_id = c.id
    """)

    dados = cursor.fetchall()

    conn.close()

    alunos = []

    for a in dados:
        alunos.append({
            "matricula": a[0],
            "nome": a[1],
            "curso": a[2]
        })

    return ordenar_por_curso(alunos)


@app.route("/notas", methods=["POST"])
def cadastrar_notas():

    dados = request.json

    conn = conectar()
    cursor = conn.cursor()

    cursor.execute("""

        SELECT id
        FROM notas
        WHERE aluno_matricula = ?

    """, (dados["aluno_matricula"],))

    nota = cursor.fetchone()

    if nota:

        conn.close()

        return {
            "erro": "Este aluno já possui notas."
        }, 400

    cursor.execute("""

        INSERT INTO notas(

            aluno_matricula,
            nota1,
            nota2,
            nota3,
            data

        )

        VALUES(?,?,?,?,?)

    """, (

        dados["aluno_matricula"],
        dados["nota1"],
        dados["nota2"],
        dados["nota3"],
        datetime.now().strftime("%d/%m/%Y")

    ))

    conn.commit()

    conn.close()

    return {
        "mensagem": "Notas cadastradas com sucesso."
    }

@app.route("/notas", methods=["GET"])
def listar_notas():

    conn = conectar()
    cursor = conn.cursor()

    cursor.execute("""
        SELECT aluno_matricula, nota1, nota2, nota3
        FROM notas
    """)

    dados = cursor.fetchall()
    conn.close()

    notas = []

    for n in dados:
        media = calcular_media(n[1], n[2], n[3])

        notas.append({
            "aluno_matricula": n[0],
            "nota1": n[1],
            "nota2": n[2],
            "nota3": n[3],
            "media": media
        })

    return notas

@app.route("/notas/<int:id>", methods=["PUT"])
def atualizar_nota(id):

    dados = request.json

    conn = conectar()
    cursor = conn.cursor()

    cursor.execute("""
        UPDATE notas
        SET nota1 = ?, nota2 = ?, nota3 = ?
        WHERE id = ?
    """, (
        dados["nota1"],
        dados["nota2"],
        dados["nota3"],
        id
    ))

    conn.commit()
    conn.close()

    return {"mensagem": "Nota atualizada com sucesso"}

@app.route("/notas/<int:id>", methods=["DELETE"])
def deletar_nota(id):

    conn = conectar()
    cursor = conn.cursor()

    cursor.execute("""
        DELETE FROM notas
        WHERE id = ?
    """, (id,))

    conn.commit()
    conn.close()

    return {"mensagem": "Nota deletada com sucesso"}


@app.route("/notas/aluno/<int:matricula>")
def notas_por_aluno(matricula):

    conn = conectar()
    cursor = conn.cursor()

    cursor.execute("""
        SELECT id, nota1, nota2, nota3
        FROM notas
        WHERE aluno_matricula = ?
    """, (matricula,))

    dados = cursor.fetchall()
    conn.close()

    if not dados:
        return {"erro": "Nenhuma nota encontrada"}

    resultado = []

    for n in dados:
       resultado.append({

    "id": n[0],

    "nota1": n[1],

    "nota2": n[2],

    "nota3": n[3],

    "media": calcular_media(
        n[1],
        n[2],
        n[3]
    )

})

    return resultado
@app.route("/notas/<int:id>", methods=["GET"])
def buscar_nota(id):

    conn = conectar()
    cursor = conn.cursor()

    cursor.execute("""
        SELECT
            id,
            aluno_matricula,
            nota1,
            nota2,
            nota3
        FROM notas
        WHERE id = ?
    """, (id,))

    nota = cursor.fetchone()

    conn.close()

    if nota is None:

        return {
            "erro": "Nota não encontrada"
        }, 404

    return {

        "id": nota[0],
        "aluno_matricula": nota[1],
        "nota1": nota[2],
        "nota2": nota[3],
        "nota3": nota[4],
        "media": calcular_media(
            nota[2],
            nota[3],
            nota[4]
        )

    }

@app.route("/relatorio")
def relatorio():

    conn = conectar()
    cursor = conn.cursor()

    # Lista de alunos
    cursor.execute("""
        SELECT
            matricula,
            nome
        FROM alunos
    """)

    alunos = []

    for a in cursor.fetchall():

        alunos.append({

            "matricula": a[0],

            "nome": a[1]

        })

    # Lista de notas
    cursor.execute("""
        SELECT
            aluno_matricula,
            nota1,
            nota2,
            nota3
        FROM notas
    """)

    notas = []

    for n in cursor.fetchall():

        notas.append({

            "aluno_matricula": n[0],

            "nota1": n[1],

            "nota2": n[2],

            "nota3": n[3]

        })

    conn.close()

    return gerar_relatorio(
        alunos,
        notas
    )

if __name__ == "__main__":
    app.run(debug=True)