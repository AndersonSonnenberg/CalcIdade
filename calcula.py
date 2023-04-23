from datetime import date
from flask import Flask, request

app = Flask(__name__)

@app.route("/")
def index():
    return "Bem-vindo à aplicação para calcular a idade!"

@app.route("/idade")
def calcular_idade():
    nome = request.args.get('nome')
    nascimento = request.args.get('nascimento')

    #Converta a data de nascimento em um objeto date
    dia, mes, ano = map(int, nascimento.split('/'))
    nascimento = date(ano, mes, dia)

    #Calcula a idade
    hoje = date.today()
    idade = hoje.year - nascimento.year - ((hoje.month, hoje.day) < (nascimento.month, nascimento.day))

    #Retorna a mensagem com a idade da pessoa
    return f"Olá {nome}, você tem {idade} anos!"

if __name__ == "__main__":
    app.run(debug=True)