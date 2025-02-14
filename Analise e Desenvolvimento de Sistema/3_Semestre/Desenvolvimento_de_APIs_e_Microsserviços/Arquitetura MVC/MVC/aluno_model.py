from flask import jsonify

database = [{"id": 1, "nome": "Andreia", "media": 8.5},
            {"id": 2, "nome": "Arthur", "media": 10},
            {"id": 3, "nome": "Pedro", "media": 10},
            {"id": 4, "nome": "Ana", "media": 7}]


def getAll():
    if database:
        return jsonify(database)
    return None


def getAlunoId(id_consulta):
    for aluno in database:
        if aluno['id'] == id_consulta:
            return aluno
    return None


def inserirAluno(aluno):
    novo_aluno = aluno
    database.append(novo_aluno)
    return


def excluirAluno(aluno):
    database.remove(aluno)


def alterarAluno(aluno, novo_aluno):
    excluirAluno(aluno)
    inserirAluno(novo_aluno)
    return


def getAlunoMaiorMedia():
    maior_media = 0
    alunos_maior_media = []
    for aluno in database:
        if aluno['media'] >= maior_media:
            if aluno['media'] > maior_media:
                alunos_maior_media = []
            maior_media = aluno['media']
            alunos_maior_media.append(aluno)

    if alunos_maior_media:
        return jsonify(alunos_maior_media)
    return None


def getAlunoMenorMedia():
    menor_media = 10000000
    alunos_menor_media = []
    for aluno in database:
        if aluno['media'] <= menor_media:
            if aluno['media'] < menor_media:
                alunos_menor_media = []
            menor_media = aluno['media']
            alunos_menor_media.append(aluno)

    if alunos_menor_media:
        return jsonify(alunos_menor_media)
    return None
