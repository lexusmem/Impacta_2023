from flask import Flask, request, jsonify
from werkzeug.exceptions import BadRequest, NotFound

app = Flask(__name__)

pessoas = dict()


def pessoa_ok(dic):
    return type(dic) == dict \
        and len(dic) == 3 \
        and "nome" in dic \
        and "sexo" in dic \
        and "cabelo" in dic \
        and type(dic["nome"]) == str \
        and dic["sexo"] in ["M", "F"] \
        and type(dic["cabelo"]) == str


@app.route("/", methods=["GET"])
def principal():
    return pessoas


@app.route("/pessoa", methods=["POST"])
def cadastrar():
    n = len(pessoas)
    pessoa = request.json
    if not pessoa_ok(pessoa):
        raise BadRequest
    pessoas[n] = pessoa
    n += 1
    return pessoas


if __name__ == "__main__":
    app.run(debug=True)
