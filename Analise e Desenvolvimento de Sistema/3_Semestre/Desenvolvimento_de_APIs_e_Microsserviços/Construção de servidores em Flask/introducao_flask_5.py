from flask import Flask

app = Flask(__name__)


@app.route("/")
def padrao():
    return 'Inicial'


# signed - permite valores negativos
@app.route("/<float(signed=True):a>/divide/<float(signed=True):b>")
@app.route("/<int(signed = True):a>/divide/<float(signed = True):b>")
@app.route("/<float(signed = True):a>/divide/<int(signed = True):b>")
@app.route("/<int(signed = True):a>/divide/<int(signed = True):b>")
def dividir(a, b):
    if b == 0.0:
        return "Não divida por zero!", 422
    return str(a / b)


if __name__ == '__main__':
    app.run(debug=True)
    # app.run(host = 'localhost', port = 5002, debug = True)
    # É possível atualizar as especificações de execução do flask.
