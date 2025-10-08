def soma(a, b):
    return a + b


# Programa principal
try:
    resultado = soma(10, 20)
    assert resultado == 30, 'Erro na soma'
    print('Soma correta!')
except AssertionError as e:
    print(f'Retorno do assert: {e}')
