def somar():
    n1 = int(input('Informe valor: '))
    n2 = int(input('Informe valor: '))
    soma = n1 + n2
    print(soma)


somar()


def somar_1(n1, n2):
    soma = n1 + n2
    print(soma)
    return


somar_1(5, 6)


def somar_2(n1, n2):
    return n1 + n2


print(somar_2(6, 6))
x = somar_2(6, 6)
print(x)


def ver_numero():
    if numero == 10:
        print('Número igual a 10.')
    else:
        print('Número diferente de 10.')


numero = 11
ver_numero()
