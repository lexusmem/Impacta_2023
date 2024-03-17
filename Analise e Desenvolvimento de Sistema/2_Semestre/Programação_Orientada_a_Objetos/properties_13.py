# Criando getter e setter de forma não habitual no python:
class Pessoa:
    def __init__(self, nome):
        self.__nome = nome

    def _get_nome(self):
        return self.__nome

    def _set_nome(self, novo_nome):
        self.__nome = novo_nome

    nome = property(_get_nome, _set_nome)


usuario_1 = Pessoa('Alex')
print(usuario_1.nome)
usuario_1.nome = 'Novo Nome'
print(usuario_1.nome)

# utilização de decoradores de forma habtual do pytho
# @property e @setter


class Pessoa2:
    def __init__(self, nome):
        self.__nome = nome

    @property
    def nome(self):
        return self.__nome

    @nome.setter
    def nome(self, novo_nome):
        self.__nome = novo_nome


usuario_2 = Pessoa2('Alex')
print(usuario_2.nome)
usuario_2.nome = 'Novo Nome'
print(usuario_2.nome)
