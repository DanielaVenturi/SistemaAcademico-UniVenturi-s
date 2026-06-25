from flask import Flask

from flask_cors import CORS

from database import criar_tabelas

app = Flask(__name__)

CORS(app)

criar_tabelas()


@app.route("/")
def home():

    return {
        "mensagem": "Sistema Academico Online"
    }


if __name__ == "__main__":
    app.run(debug=True)