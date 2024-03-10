def exibe_nome():
    print(f'O nome deste módulo é: {__name__!r}')


def impressao_teste():
    print('Teste de impressão')


variavel = 10


class Teste:
    pass


__all__ = ['exibe_nome', 'impressao_teste']

if __name__ == '__main__':
    exibe_nome()
