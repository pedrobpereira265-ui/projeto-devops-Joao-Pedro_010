import os

from flask import Flask, jsonify
# ===== VARIAÇÃO DA DUPLA (mude estes valores) =====
NOME_DUPLA = "projeto-devops-Joao-Pedro_010"

MENSAGEM = "Olá Mundo, está um belo dia lá fora!"

PORTA = 8000
# ==================================================
VERSAO = os.environ.get("APP_VERSION", "v1")

app = Flask(__name__)

@app.route("/saude")
def saude():
 return jsonify(status="ok", versao=VERSAO)

@app.route("/aluno")
def aluno():
 return jsonify(dupla=NOME_DUPLA, mensagem=MENSAGEM)

@app.route("/")
def inicio():
    return "Projeto DevOps funcionando!"
if __name__ == "__main__":
 app.run(host="0.0.0.0", port=PORTA)