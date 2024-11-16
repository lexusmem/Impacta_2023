from flask import Flask, request

app = Flask('__name__')


@app.route('/', methods=['POST'])
def start():
    nome = request.get_json(force=True)
    return f"Seja Bem-Vindo, {nome}, na aula de desenvolvimento de API's e Microsserviços."


if __name__ == '__main__':
    app.run(debug=True)
