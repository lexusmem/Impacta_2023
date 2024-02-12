class Teste:
    def __init__(self):
        self.__nome = ''
        self.cont = 0

    @property
    def nome(self):
        self.cont += 1
        print(f'executando a property...{self.cont}')
        return self.__nome

    @nome.setter
    def nome(self, novo_nome):
        print('executando a setter...')
        self.__nome = novo_nome


if __name__ == '__main__':
    nome_1 = Teste()
    print(nome_1.nome)
    nome_1.nome = 'Alex'
    print(nome_1.nome)
    print(vars(nome_1))
