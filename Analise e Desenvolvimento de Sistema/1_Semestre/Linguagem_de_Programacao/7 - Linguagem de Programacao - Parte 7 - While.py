# p = int(input('Digite um valor para p: '))
# q = int(input('Digite um valor para q: '))

# contador = 0

# while p >= q:
#     p -= q
#     contador += 1

# print(f'O quocienta da divisão é {contador}.')

# soma = 0
# qtd = 0

# n = int(input('Digite um número: '))
# while n != -1:
#     soma += n
#     qtd += 1
#     n = int(input('Digite um número: '))
# print(f'Média {soma/qtd}')


# total = 0
# quero_comprar = True

# while quero_comprar:
#     preco = float(input('Digite o valor do produto: '))
#     total = + preco
#     opcao = input('Continuar comprando (s/n)? ')
#     opcao = opcao.lower()
#     if opcao != 's':
#         quero_comprar = False

# print(f'O total da compra foi R${total: .2f}')

# 2) Crie um programa que exiba todos os números inteiros de 100 até 200 em
#  ordem crescente depois crie outro programa que exiba de 200 até 100 em
# ordem decrescente.

num_ini = 100
num_fim = 200

while num_ini <= num_fim:
    print(num_ini)
    num_ini += 1

print("---------------------")

num_ini = 100
num_fim = 200

while num_fim >= num_ini:
    print(num_fim)
    num_fim -= 1

'''
3) Crie um programa que leia um número natural n
dado pelo usuário e exiba só os n primeiros pares a
 partir do 0. Por exemplo, se n=6 será exibido 0 2 4 6 8 10.
 '''
n = int(input('Digite um número: '))
contador = 0
num_par = 0

while contador < n:
    print(num_par, " ")
    num_par += 2
    contador += 1

'''
4) Crie um programa que solicite ao usuário dois números naturais 
x e y, o programa deverá exibir o quociente da divisão inteira de
x por y sem usar os operadores de divisão e multiplicação. Por 
exemplo, se x=7 e y=2 a resposta será 3, pois podemos raciocinar
que o quociente da divisão inteira de x por y é dado pela quantidade
de vezes que y pode ser subtraído de x sem que x se torne negativo.
'''
x = int(input('Digite um número X: '))
y = int(input('Digite um número Y: '))
quociente = 0
div = 0

while x >= y:
    x -= y
    quociente += 1

print(quociente)

'''5) Crie um programa que peça letras como entrada,
uma por vez, até que seja lida a letra 'x', ao final,
o programa deve exibir a quantidade de letras lidas 
sem contabilizar 'x'. Observação: lembre-se que o 
Python diferencia maiúsculas e minúsculas.'''

letra = input('Digite uma letra qualquer, para para digite "x": ')
contador = 0

while letra.lower() != 'x':
    contador += 1
    letra = input('Digite uma letra qualquer, para para digite "x": ')

print(f"Foi digitado um total de {contador} letras.")
