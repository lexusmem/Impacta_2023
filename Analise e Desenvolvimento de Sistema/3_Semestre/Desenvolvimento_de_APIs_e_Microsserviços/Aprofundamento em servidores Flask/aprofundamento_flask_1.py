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
def principal():
    return 'Rota Principal.'


@app.route("/frutas/<nome_fruta>/cor")
def frutas(nome_fruta):
    if nome_fruta in cores_frutas:
        return cores_frutas[nome_fruta]
    return "Não sei."


if __name__ == "__main__":
    app.run(debug=True)
