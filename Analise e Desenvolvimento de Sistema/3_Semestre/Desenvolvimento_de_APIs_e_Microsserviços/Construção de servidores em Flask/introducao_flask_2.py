from flask import Flask

app = Flask(__name__)

cores_frutas = {
    "morango": "vermelho",
    "uva": "roxo",
    "banana": "amarelo",
    "abacaxi": "amarelo",
    "limão": "verde"
}


@app.route("/")
def padrao():
    return 'Inicial'


@app.route('/frutas/<nome_fruta>/cor')
def cor_frutas(nome_fruta):
    if nome_fruta in cores_frutas:
        return cores_frutas[nome_fruta]
    else:
        return 'Não possui está fruta'


if __name__ == '__main__':
    app.run(debug=True)
    # app.run(host = 'localhost', port = 5002, debug = True)
    # É possível atualizar as especificações de execução do flask.
