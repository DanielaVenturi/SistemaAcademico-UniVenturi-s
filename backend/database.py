import sqlite3

def conectar():
    return sqlite3.connect("banco.db")


def criar_tabelas():

    conn = conectar()
    cursor = conn.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS cursos(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nome TEXT NOT NULL UNIQUE
        )
    """)

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS alunos(
            matricula INTEGER PRIMARY KEY,
            nome TEXT NOT NULL,
            curso_id INTEGER,
            FOREIGN KEY(curso_id) REFERENCES cursos(id)
        )
    """)

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS notas(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            aluno_matricula INTEGER,
            nota1 REAL,
            nota2 REAL,
            nota3 REAL,
            FOREIGN KEY(aluno_matricula) REFERENCES alunos(matricula)
        )
    """)

    conn.commit()
    conn.close()