# Crie um programa que exiba sequencia crescente.
n = int(input('Informe um valor: '))

for index, valor in enumerate(range(1, n+1)):
    print(valor, index, end=" ")
print("\n")

# Crie um programa que exiba valores pares.
n_1 = int(input('Informe um valor: '))

for valor in range(0, n_1+1, 2):
    print(valor, end=" ")
print("\n")

# Crie um programa que exiba sequencia decrescente.
n_2 = int(input('Informe um valor: '))

for valor in range(n_2, 0, -1):
    print(valor, end=" ")
print("\n")

# criar programa que exiba os dias da semana
dias = ['domingo', 'segunda', 'terça', 'quarta', 'quinta', 'sexta', 'sábado']

for i, dia in enumerate(dias):
    print(f'índice {i}, dia da semana - {dia}.')

# Refaça a solução da Codificação 9.6 para dois novos cenários:
'''1) O programa perguntará quantos salários serão inseridos, em 
seguida receberá cada salário, calculará a média e exibirá todos
 os salários que sejam inferiores à média. '''

salarios = []
qtd_salarios = int(input('Informe a quantidade de salários: '))
soma = 0

for _ in range(qtd_salarios):
    salario = float(input('Informe o valor do salário: '))
    salarios.append(salario)
    soma += salario

media = soma / qtd_salarios

for valor in salarios:
    if valor < media:
        print(f'Salário R${valor: .2f} menor que a média.')

print(f'A média salarial é de R$ {media: .2f}.')

'''2) O programa receberá os salários indefinidamente, até que o
usuário digite o valor -1 como salário. Então o programa deve 
seguir o restante do fluxo, calcular a média e exibir todos os 
salários inferiores, como no cenário 1. Neste caso, será necessário
usar while, pois a quantidade de salários não está definida 
antes da execução do laço.'''

salarios_2 = []
soma_salario = 0
qtd_salarios_2 = 0
print('{:=^40}'.format('Programa 2'))
while True:
    salario_2 = float(input('Informe o valor do salário: '))
    if salario_2 <= 0:
        break
    salarios_2.append(salario_2)
    soma_salario += salario_2
    qtd_salarios_2 += 1

media_2 = soma_salario / qtd_salarios_2

for valor in salarios_2:
    if valor < media_2:
        print(f'Salário R${valor: .2f} menor que a média.')

print(f'A média salarial é de R$ {media_2: .2f}.')
