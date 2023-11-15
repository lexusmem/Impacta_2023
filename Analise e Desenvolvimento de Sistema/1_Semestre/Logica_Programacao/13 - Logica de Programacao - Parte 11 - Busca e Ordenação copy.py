# Número Primo.

numero = int(input('Informe um número: '))
contador = 0

for num in range(numero):
    div = num + 1
    if numero % div == 0:
        contador += 1

if contador == 2:
    print(f'O numero {numero} é primo')
else:
    print(f'O numero {numero} não é primo')


# Busca linear
def busca(numero, lista):
    for i, num in enumerate(lista):
        if num == numero:
            return i
    return -1


lista = [1, 3, 4, 6, 43, 22, 33, 54, 9, 67, 8]
numero_busca = int(input('Informe o numero para busca: '))

buscar = busca(numero_busca, lista)

if buscar == -1:
    print(f'O número {numero_busca} não encontrado na lista.')
else:
    print(f'O número {numero_busca} encontrado na posição {buscar}.')
