from flask import Flask, jsonify, Blueprint

alunos_app = Blueprint('alunos_app', __name__, template_folder='templetes')


database = {
    'ALUNO': [
        {'id': 1, 'nome': 'Alex'},
        {'id': 2, 'nome': 'Laura'},
        {'id': 3, 'nome': 'Pamela'}]
}


# para OBTER dados utiliza metodo GET
@alunos_app.route('/alunos', methods=['GET'])
def getAlunos():
    return jsonify(database['ALUNO'])
