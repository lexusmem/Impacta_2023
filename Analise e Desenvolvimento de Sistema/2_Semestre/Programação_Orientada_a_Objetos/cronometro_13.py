from time import perf_counter, sleep


def cronometro(f):
    def envelope(*args, **kwargs):
        t1 = perf_counter()
        r = f(*args, **kwargs)
        t2 = perf_counter()
        print(f'{f.__name__} executando em {t2 - t1:.4e} segundos.')
        return r
    return envelope


@cronometro
def funcao_exemplo():
    print('Executando Função Exemplo para contagem de tempo de execução.')
    sleep(2)


funcao_exemplo()

# Outra forma de decorar a função exemplo seria utilizando o decorador @
# que polparia linhas de codificação, como por exemplo

# Abaixo mesmo código sem o decorador '@':
# def funcao_exemplo():
#     print('Executando Função Exemplo para contagem de tempo de execução.')
#     sleep(2)
# chamando a função exemplo sem estarmos decorando ela com a função cronometro.
# funcao_exemplo()
# decorando a função exemplo com a função cronometro.
# funcao_exemplo = cronometro(funcao_exemplo)
# funcao_exemplo()
