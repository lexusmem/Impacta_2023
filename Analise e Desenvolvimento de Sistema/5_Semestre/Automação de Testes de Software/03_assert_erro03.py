def soma(a, b):
    print(a + b)


# Programa principal
try:
    resultado = soma(10, 20)
    assert resultado == 30, "Soma errada!"
    print('Soma correta!')
except AssertionError as e:
    print(f'Retorno do assert: {e}')
