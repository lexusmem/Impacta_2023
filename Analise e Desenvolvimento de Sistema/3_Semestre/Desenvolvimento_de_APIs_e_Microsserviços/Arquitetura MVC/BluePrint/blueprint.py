from blueprint_alunos_api import alunos_app
from blueprint_professores_api import professores_app
import sys
import os
from flask import Flask, jsonify, Blueprint

# Caminho para o diretório onde está o módulo professores_api
caminho = r'C:\Users\lexus\Documents\Estudos\Impacta_2023\Analise e Desenvolvimento de Sistema\\3_Semestre\Desenvolvimento_de_APIs_e_Microsserviços\Arquitetura MVC\BluePrint'

# Adiciona o caminho ao sys.path
if caminho not in sys.path:
    sys.path.append(caminho)

app = Flask(__name__)

app.register_blueprint(alunos_app)
app.register_blueprint(professores_app)

if __name__ == '__main__':
    app.run(debug=True)
