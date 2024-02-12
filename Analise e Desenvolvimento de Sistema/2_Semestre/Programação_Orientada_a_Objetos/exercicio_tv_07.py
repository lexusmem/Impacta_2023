class TV:
    def __init__(self, fabricante, modelo, tela, preco):
        self.__fabricante = fabricante
        self.__modelo = modelo
        self.__tela = tela
        self.__preco = preco

    @property
    def dados_tv(self):
        print(f'Fabricante: {self.__fabricante}')
        print(f'Modelo: {self.__modelo}')
        print(f'Tela: {self.__tela}')
        print(f'Preço: {self.__preco:.2f}')

    def aplicar_desconto(self, percentual):
        if percentual > 100 or percentual < 0:
            return print('Percentual de desconto incorreto. Não pode ser'
                         ' superior a 100% ou inferior a 0%.')
        valor_ajuste = 1 - (percentual / 100)
        valor_anterior = self.__preco
        self.__preco = self.__preco * valor_ajuste
        valor_desconto = valor_anterior - self.__preco
        return print(f'Preço da TV atualizado. Valor do Desconto'
                     f' {valor_desconto:.2f}')


if __name__ == '__main__':
    tv1 = TV('Samsung', "KMLJS", 57, 2100.50)
    tv2 = TV('LG', "PKTX", 85, 6500.75)

    tv1.dados_tv
    tv1.aplicar_desconto(15)
    tv1.dados_tv
