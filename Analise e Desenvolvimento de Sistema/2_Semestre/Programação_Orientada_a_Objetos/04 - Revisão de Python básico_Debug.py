def dobrar(x):
    '''
    Função que recebe um numero e duplica o valor.
    Argumentos:
    x: Um número
    Retorno:
    Valor multiplicado por 2.
    '''
    return x * 2


def triplicar(x):
    '''
    Função que recebe um numero e triplica o valor.
    Argumentos:
    x: Um número
    Retorno:
    Valor multiplicado por 3.
    '''
    triplo = x * 3
    return triplo


num = float(input('Digite um número: '))
dobro = dobrar(num)
print(f'O dobro de {num} é: {dobro}')
print(f'O triplo de {num} é: {triplicar(num)}')
