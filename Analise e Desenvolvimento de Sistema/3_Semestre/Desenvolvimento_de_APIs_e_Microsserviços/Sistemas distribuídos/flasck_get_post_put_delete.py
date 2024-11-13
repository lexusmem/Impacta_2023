from flask import Flask, jsonify, request

app = Flask(__name__)

database = {
    'ALUNO': [
        {'id': 1, 'nome': 'Alex'},
        {'id': 2, 'nome': 'Laura'},
        {'id': 3, 'nome': 'Pamela'}
    ],
    'PROFESSOR': [
        {'id': 1, 'nome': 'Professor_1'},
        {'id': 2, 'nome': 'Professor_2'},
        {'id': 3, 'nome': 'Professor_3'}
    ]
}


@app.route('/')
def start():
    return 'Vamos integrar Requests e Flask'


# para OBTER dados utiliza metodo GET
@app.route('/alunos', methods=['GET'])
def getAlunos():
    return jsonify(database['ALUNO'])


@app.route('/alunos', methods=['POST'])
def inputAlunos():
    novo_aluno = request.json
    database['ALUNO'].append(novo_aluno)
    return jsonify(database['ALUNO'])


@app.route('/alunos/<int:id_aluno>', methods=['DELETE'])
def deleteAlunos(id_aluno):
    for aluno in database['ALUNO']:
        if aluno['id'] == id_aluno:
            database['ALUNO'].remove(aluno)
            return jsonify(database['ALUNO'])
    return 'Aluno não Localizado', 404


@app.route('/alunos/<int:id_aluno>', methods=['PUT'])
def alteraAlunos(id_aluno):
    atualiza_aluno = request.get_json()
    for aluno in database['ALUNO']:
        if aluno['id'] == id_aluno:
            database['ALUNO'].remove(aluno)
            database['ALUNO'].append(atualiza_aluno)
            return jsonify(database['ALUNO'])
    return 'Aluno não Localizado', 404


@app.route('/alunos/<int:id_aluno>', methods=['GET'])
def getAluno(id_aluno):
    for aluno in database['ALUNO']:
        if aluno['id'] == id_aluno:
            return jsonify(aluno)
    return 'Aluno não Localizado', 404


@app.route('/professor', methods=['GET'])
def getProfessor():
    return jsonify(database['ALUNO'])


@app.route('/resetar', methods=['POST'])
def zerar_dados():
    database['ALUNO'] = []
    database['PROFESSOR'] = []
    return jsonify(database)


@app.route('/todos', methods=['GET'])
def getAll():
    return jsonify(database)


if __name__ == '__main__':
    app.run(debug=True)
