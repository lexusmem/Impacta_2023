# variável __name__
# todo modulo tem um nome em python.
# a variável especial __name__ desempenha um papel importante na diferenciação
# entre a execução de um módulo como script principal e sua importação como
# parte de outro código.
import meu_modulo_09


def exibe_nome():
    print(f'O nome deste módulo é: {__name__!r}')


if __name__ == '__main__':
    exibe_nome()

# quando é executo o próprio arquivo que consta a função o nome daquele modulo
# é main, porém se é chamado o módulo de outro arquivo o name é o nome do
# próprio módulo.

# exemplo:
meu_modulo_09.exibe_nome()
