import aluno_model as aluno_model
import sys
import os

# Caminho para o diretório onde está o módulo MVC
caminho = r'C:\Users\lexus\Documents\Estudos\Impacta_2023\Analise e Desenvolvimento de Sistema\\3_Semestre\Desenvolvimento_de_APIs_e_Microsserviços\Arquitetura MVC\MVC'

if caminho not in sys.path:
    sys.path.append(caminho)


# listar todos os alunos do database
def listar():
    alunos = aluno_model.getAll()
    if alunos == None:
        return 'Não existem alunos cadastrados. Verifique!'
    return alunos


def localizaPorId(id_consulta):
    aluno = aluno_model.getAlunoId(id_consulta)
    if aluno == None:
        return 'Aluno não encontrado'
    return {"Status": "Aluno encontrado", "Aluno": aluno}


def localizarPorMaiorMedia():
    alunos = aluno_model.getAlunoMaiorMedia()
    return alunos


def localizarPorMenorMedia():
    alunos = aluno_model.getAlunoMenorMedia()
    return alunos


def inserirAluno(aluno):
    aluno_model.inserirAluno(aluno)
    return listar()


def excluirPorId(id_deletar):
    aluno = aluno_model.getAlunoId(id_deletar)
    if aluno == None:
        return 'Aluno não encontrado'

    aluno_model.excluirAluno(aluno)
    return listar()


def alterarAluno(id_alterar, novo_aluno):
    aluno = aluno_model.getAlunoId(id_alterar)
    if aluno == None:
        return 'Aluno não encontrado'

    aluno_model.alterarAluno(aluno, novo_aluno)
    return listar()


'''
def localizar(id):
    aluno = dao_consultar(id)
    if aluno == None:
        return None
    return aluno.__dict__()
'''
