from flask import Flask

app = Flask(__name__)


@app.route("/")
def padrao():
    return 'Inicial'


@app.route("/<float:a>/menos/<float:b>")
def subtrair(a, b):
    return str(a - b)


fib = [0, 1]


def fibonacci(valor):
    while valor >= len(fib):
        fib.append(fib[-1] + fib[-2])
    return fib[valor]


@app.route("/fibonacci/<int:valor>")
def num_fibonacci(valor):
    return f"O {valor}º valor da sequência de " \
        + f"Fibonacci é {fibonacci(valor)}."


if __name__ == '__main__':
    app.run(debug=True)
    # app.run(host = 'localhost', port = 5002, debug = True)
    # É possível atualizar as especificações de execução do flask.
