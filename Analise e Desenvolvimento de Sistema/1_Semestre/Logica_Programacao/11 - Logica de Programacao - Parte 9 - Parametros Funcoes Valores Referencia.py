# Em python tuplas, listas e dicionários
# são enviados como parâmetros de funções
# por referencia.


# Parâmetro por Valor
def parametro_valor(a):
    a = 'x'
    print(a)
    print(f'O endereço da variável "a" no escopo local é {id(a)}')


a = 2

print(a)
print(f'O endereço da variável "a" no escopo globa é {id(a)}')
parametro_valor(2)
print(a)
print(f'O endereço da variável "a" no escopo globa é {id(a)}')
print()


# Parâmetro por Referencia
def parametro_referencia(r):
    for i, n in enumerate(r):
        print(f'O endereço da variável "r" no escopo local é {id(r)}')
        r[i] = n * 5
        print(i, r[i])


r = [1, 2, 3, 4]

for i, n in enumerate(r):
    print(f'O endereço da variável "r" no escopo global é {id(r)}')
    print(i, n)

parametro_referencia(r)

print(r)
