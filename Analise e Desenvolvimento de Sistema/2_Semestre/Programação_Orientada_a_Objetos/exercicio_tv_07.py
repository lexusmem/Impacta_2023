class TV:
    def __init__(self, fabricante, modelo, tela, preco):
        self.__fabricante = fabricante
        self.__modelo = modelo
        self.__tela = tela
        self.__preco = preco

    @property
    def dados_tv(self):
        return {'Fabricante': self.__fabricante,
                'Modelo': self.__modelo,
                'Tela': self.__tela,
                'Preço': self.__preco}

    @property
    def valor_tv(self):
        return self.__preco

    @valor_tv.setter
    def valor_tv(self, novo_preco):
        self.__preco = novo_preco

    def set_aplicar_desconto(self, percentual):
        if percentual > 100 or percentual < 0:
            return print('Percentual de desconto incorreto. Não pode ser'
                         ' superior a 100% ou inferior a 0%.')
        valor_ajuste = 1 - (percentual / 100)
        valor_anterior = self.__preco
        self.valor_tv = self.__preco * valor_ajuste
        valor_desconto = valor_anterior - self.__preco
        return print(f'Preço da TV atualizado. Valor do Desconto'
                     f' {valor_desconto:.2f}')


if __name__ == '__main__':
    tv1 = TV('Samsung', "KMLJS", 57, 2100.50)
    tv2 = TV('LG', "PKTX", 85, 6500.75)

    print(tv1.dados_tv)
    tv1.set_aplicar_desconto(15)
    print(tv1.dados_tv)
    print(f'{tv1.valor_tv:.2f}')

    for x, a in tv1.dados_tv.items():
        print(f'{x}: {a}')

    print(type(tv1.dados_tv))
    print(type(tv1.valor_tv))

    tv1.valor_tv = 2700.00
    print(f'{tv1.valor_tv:.2f}')
