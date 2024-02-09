# estrutura de seleção

n = int(input('Digite um número: '))

# if sem elif
if n > 10:
    print('Valor informado é maior que 10.')
else:
    if n == 10:
        print('O Valor informado é igual a 10.')
    else:
        print('O Valor informado é menor que 10.')

# if com elif
if n > 10:
    print('Valor informado é maior que 10.')
elif n == 10:
    print('O Valor informado é igual a 10.')
else:
    print('O Valor informado é menor que 10.')
