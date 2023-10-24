# Importação de bibliotecas python
# Importações ###
import math
import time

time.sleep(1)
print(math.pi)
print(math.log(10))

print(type(time))

# Definição de funções
# Funções ###


def nome_da_funcao(parametro_nome):
    '''
    Função que retorna mensagem com o nome informado
    '''
    print(f'Olá {parametro_nome}!')


def soma(num1, num2):
    '''
    Função que retorna a soma de dois números.
    '''
    soma = num1 + num2
    return soma


def pede_idade():
    '''
    Função que solicitada idade do usuário
    '''
    idade = int(input('Digite sua idade: '))
    return idade


def verifica_se_maior(idade):
    '''
    Função que verifica se é de maior.
    '''
    if idade >= 18:
        print('Você é de maior!')
    else:
        print('Você é de menor!')


# Código Principal ###
print(help(nome_da_funcao))
print(nome_da_funcao('Alex'))

print(help(soma))
print(soma(10, 22))

a = int(input('Digite um número: '))
somar = soma(a, math.pi)

print(f'{a} + {math.pi:.3f} = {somar:.3f}')

idade = pede_idade()
print(help(pede_idade))
print(f'A idade digitada foi {idade}.')
print(help(verifica_se_maior))
verifica_se_maior(idade)
