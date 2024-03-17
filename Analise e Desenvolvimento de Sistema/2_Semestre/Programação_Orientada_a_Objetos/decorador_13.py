def decorador(f):
    def envelope():
        print('Código executado antes de chamar f.')
        f()
        print('Código executado após chamar f.')
    return envelope

# def ola_mundo():
#     print('Olá Mundo!')

# print(ola_mundo)
# ola_mundo()
# print('\n')
# ola_mundo = decorador(ola_mundo)
# print(ola_mundo)
# ola_mundo()


@decorador
def ola_mundo():
    print('Olá Mundo!')

# porem estas atribuições não são acima não são necessárias se utilizarmos o decorador @ do python na função.


if __name__ == '__main__':
    print(ola_mundo)
    ola_mundo()
