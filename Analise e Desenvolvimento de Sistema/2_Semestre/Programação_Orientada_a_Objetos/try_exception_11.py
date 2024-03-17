from exception_raise_error_11 import Paciente, NameIsEmptyError

try:
    nome = input('Digite o nome do paciente: ')
    paciente_1 = Paciente(nome)
    paciente_1.paciente = ""
except TypeError:
    print('O nome deve ser uma string.')
except NameIsEmptyError:
    print('O nome não pode ser uma string vazia.')
except Exception as e:
    print('Ocorreu um erro inesperado ao criar o objeto Paciente.')
    print('Informação do erro: ', e)
else:
    print('Se estiver aqui, não ocorreu erro no try!')
finally:
    print('Finally - sempre será executado.')
