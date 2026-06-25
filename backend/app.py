from flask import Flask, request
from flask_cors import CORS
from busca import busca_por_nome, busca_por_matricula
from database import criar_tabelas, conectar

app = Flask(__name__)

CORS(app)

criar_tabelas()


@app.route("/")
def home():
    return {
        "mensagem": "Sistema Academico Online"
    }


@app.route("/alunos", methods=["POST"])
def cadastrar_aluno():

    dados = request.json

    conn = conectar()
    cursor = conn.cursor()

    cursor.execute("""
        INSERT INTO alunos
        (matricula, nome, curso)
        VALUES (?, ?, ?)
    """, (
        dados["matricula"],
        dados["nome"],
        dados["curso"]
    ))

    conn.commit()
    conn.close()

    return {
        "mensagem": "Aluno cadastrado com sucesso"
    }


@app.route("/alunos", methods=["GET"])
def listar_alunos():

    conn = conectar()
    cursor = conn.cursor()

    cursor.execute("""
        SELECT matricula, nome, curso
        FROM alunos
    """)

    resultado = cursor.fetchall()

    conn.close()

    alunos = []

    for aluno in resultado:

        alunos.append({
            "matricula": aluno[0],
            "nome": aluno[1],
            "curso": aluno[2]
        })

    return alunos


if __name__ == "__main__":
    app.run(debug=True)

@app.route("/alunos/busca/<nome>")
def buscar_aluno(nome):

    conn = conectar()
    cursor = conn.cursor()

    cursor.execute("""
        SELECT matricula, nome, curso
        FROM alunos
    """)

    dados = cursor.fetchall()

    conn.close()

    alunos = []

    for aluno in dados:

        alunos.append({
            "matricula": aluno[0],
            "nome": aluno[1],
            "curso": aluno[2]
        })

    resultado = busca_por_nome(alunos, nome)

    return resultado

@app.route("/alunos/matricula/<int:matricula>")
def buscar_matricula(matricula):

    conn = conectar()
    cursor = conn.cursor()

    cursor.execute("""
        SELECT matricula, nome, curso
        FROM alunos
    """)

    dados = cursor.fetchall()

    conn.close()

    alunos = []

    for aluno in dados:

        alunos.append({
            "matricula": aluno[0],
            "nome": aluno[1],
            "curso": aluno[2]
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