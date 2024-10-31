from flask import Flask

app = Flask(__name__)


# posso definir duas rotas para mesma função.
@app.route("/")
@app.route("/sejabemvindo")
def boasvinda():
    return 'Seja Bem-Vindo'


# Criação de diversas rotas.
@app.route("/boatarde")
def boatarde():
    return 'Boa Tarde'


@app.route("/um/caminho/longo")
def caminho_longo():
    return 'Olá caminho'


if __name__ == '__main__':
    app.run(debug=True)
    # app.run(host = 'localhost', port = 5002, debug = True)
    # É possível atualizar as especificações de execução do flask.
