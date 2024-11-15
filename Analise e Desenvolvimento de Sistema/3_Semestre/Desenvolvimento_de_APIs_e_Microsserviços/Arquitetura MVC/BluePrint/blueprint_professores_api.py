from flask import Flask, jsonify, Blueprint

professores_app = Blueprint(
    'professores_app', __name__, template_folder='templetes')

database = {
    'PROFESSOR': [
        {'id': 1, 'nome': 'Professor_1'},
        {'id': 2, 'nome': 'Professor_2'},
        {'id': 3, 'nome': 'Professor_3'}
    ]
}


@professores_app.route('/professor', methods=['GET'])
def getProfessor():
    return jsonify(database['PROFESSOR'])
