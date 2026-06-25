from flask import Flask, request
from flask_cors import CORS

from database import criar_tabelas, conectar
from busca import busca_por_nome, busca_por_matricula
from ordenacao import ordenar_por_nome, ordenar_por_matricula
from relatorios import calcular_media

app = Flask(__name__)
CORS(app)

criar_tabelas()

print("APP ATUALIZADO CARREGADO")


@app.route("/")
def home():
    return {"mensagem": "Sistema Acadêmico Online"}


@app.route("/alunos", methods=["POST"])
def cadastrar_aluno():

    dados = request.json

    conn = conectar()
    cursor = conn.cursor()

    cursor.execute("""
        INSERT INTO alunos (matricula, nome, curso)
        VALUES (?, ?, ?)
    """, (
        dados["matricula"],
        dados["nome"],
        dados["curso"]
    ))

    conn.commit()
    conn.close()

    return {"mensagem": "Aluno cadastrado com sucesso"}


@app.route("/alunos", methods=["GET"])
def listar_alunos():

    conn = conectar()
    cursor = conn.cursor()

    cursor.execute("SELECT matricula, nome, curso FROM alunos")
    dados = cursor.fetchall()
    conn.close()

    alunos = [
        {"matricula": a[0], "nome": a[1], "curso": a[2]}
        for a in dados
    ]

    return alunos


@app.route("/alunos/busca/<nome>")
def buscar_por_nome(nome):

    conn = conectar()
    cursor = conn.cursor()

    cursor.execute("SELECT matricula, nome, curso FROM alunos")
    dados = cursor.fetchall()
    conn.close()

    alunos = [
        {"matricula": a[0], "nome": a[1], "curso": a[2]}
        for a in dados
    ]

    return busca_por_nome(alunos, nome)


@app.route("/alunos/matricula/<int:matricula>")
def buscar_por_matricula(matricula):

    conn = conectar()
    cursor = conn.cursor()

    cursor.execute("SELECT matricula, nome, curso FROM alunos")
    dados = cursor.fetchall()
    conn.close()

    alunos = [
        {"matricula": a[0], "nome": a[1], "curso": a[2]}
        for a in dados
    ]

    resultado = busca_por_matricula(alunos, matricula)

    if resultado:
        return resultado

    return {"erro": "Aluno não encontrado"}, 404


@app.route("/alunos/ordenados")
def alunos_ordenados():

    conn = conectar()
    cursor = conn.cursor()

    cursor.execute("SELECT matricula, nome, curso FROM alunos")
    dados = cursor.fetchall()
    conn.close()

    alunos = [
        {"matricula": a[0], "nome": a[1], "curso": a[2]}
        for a in dados
    ]

    return ordenar_por_nome(alunos)


@app.route("/notas", methods=["POST"])
def cadastrar_notas():

    dados = request.json

    conn = conectar()
    cursor = conn.cursor()

    cursor.execute("""
        INSERT INTO notas (aluno_matricula, nota1, nota2, nota3)
        VALUES (?, ?, ?, ?)
    """, (
        dados["aluno_matricula"],
        dados["nota1"],
        dados["nota2"],
        dados["nota3"]
    ))

    conn.commit()
    conn.close()

    return {"mensagem": "Notas cadastradas com sucesso"}


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


@app.route("/notas/aluno/<int:matricula>")
def notas_por_aluno(matricula):

    conn = conectar()
    cursor = conn.cursor()

    cursor.execute("""
        SELECT nota1, nota2, nota3
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
            "nota1": n[0],
            "nota2": n[1],
            "nota3": n[2],
            "media": calcular_media(n[0], n[1], n[2])
        })

    return resultado


if __name__ == "__main__":
    app.run(debug=True)