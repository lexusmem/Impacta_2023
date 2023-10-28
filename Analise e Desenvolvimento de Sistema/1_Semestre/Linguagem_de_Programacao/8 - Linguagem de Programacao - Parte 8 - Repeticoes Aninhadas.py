from math import sqrt
# BREAK encerra o programa.

# PROGRAMA PARA VERIFICAR NUMERO PRIMO.

# Um número primo é aquele que é dividido apenas por um
#  e por ele mesmo. Entre 0 e 100 existem apenas 25 números primos

num = int(input('Informe um número: '))
divisor = 2
contador = 0

while divisor < num:
    if num % divisor == 0:
        break
    divisor += 1

if divisor == num or num == 1:
    print(f'O número {num} é primo.')
else:
    print(f'O número {num} não é primo.')

# Repeat...Until
while True:
    n = float(input('Número para cálculo da raiz quadrada: '))
    if n >= 0:
        break

print(f'Raiz quadrada de {n} é igual{sqrt(n): .3f}.')


# Laços Aninhados
# def relogio():
#     h = 0
#     while h < 24:
#         m = 0
#         while m < 60:
#             s = 0
#             while s < 60:
#                 print(f"{h: 02}: {m: 02}: {s: 02}")
#                 s += 1
#             m += 1
#         h += 1


# relogio()

# 1) crie uma função que receba como argumento um número natural e exiba seus
# dígitos na ordem do último
# para o primeiro, porém usando a estrutura de repetição while tradicional
# , sem usar if e break. Observe no Python Tutor o fluxo de execução de ambas
# as soluções.
# Por fim, discuta com seus colegas sobre a legibilidade de ambas versões e
# quais são as possíveis vantagens e desvantagens de cada abordagem.

numero = int(input('Digite um número: '))
while numero >= 0:
    print(numero, end=" ")
    numero -= 1
