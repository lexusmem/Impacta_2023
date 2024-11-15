import aluno_controller as aluno_controller
import sys
import os
from flask import Flask
from flask import jsonify
from flask import request

# Caminho para o diretório onde está o módulo MVC
caminho = r'C:\Users\lexus\Documents\Estudos\Impacta_2023\Analise e Desenvolvimento de Sistema\\3_Semestre\Desenvolvimento_de_APIs_e_Microsserviços\Arquitetura MVC\MVC'

if caminho not in sys.path:
    sys.path.append(caminho)

app = Flask(__name__)


@app.route('/')
def start():
    return "Construindo nossa aplicação com MVC"


@app.route('/alunos')
def getAlunos():
    return aluno_controller.listar()


@app.route("/alunos/<int:id_consulta>", methods=["GET"])
def getAlunoId(id_consulta):
    return aluno_controller.localizaPorId(id_consulta)


@app.route("/alunos/maior_media", methods=["GET"])
def getAlunoMaiorMedia():
    return aluno_controller.localizarPorMaiorMedia()


@app.route("/alunos/menor_media", methods=["GET"])
def getAlunoMenorMedia():
    return aluno_controller.localizarPorMenorMedia()


@app.route("/alunos", methods=["POST"])
def inserir():
    aluno = request.json
    return aluno_controller.inserirAluno(aluno)


@app.route("/alunos/<int:id_deletar>", methods=["DELETE"])
def excluir(id_deletar):
    return aluno_controller.excluirPorId(id_deletar)


@app.route("/alunos/<int:id_alterar>", methods=["PUT"])
def alterar(id_alterar):
    aluno = request.json
    return aluno_controller.alterarAluno(id_alterar, aluno)


if __name__ == '__main__':
    app.run(debug=True)
