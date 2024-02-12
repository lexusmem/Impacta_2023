class Conta:
    def __init__(self, numero, titular):
        self.numero = numero
        self.titular = titular
        self.__saldo = 0

# em python todos os atributos são públicos
# mas possui convenções para tratar como privado
# tratar um atributo como privado
# exemplo: self.__saldo
# Em python é possível acessar diretamente o atributo
# com uma nova nomenclatura exemplo: self.__saldo passa a ser
# _Conta__saldo
# Com o atributo privado somente iremos acessar com métodos ou
# propriedades.


# LISTA DE MÉTODOS:

    # Método assessor
    # Método para acessar um valor get/ver
    # def get_saldo(self):
    #     return f'Seu Saldo é de {self.__saldo:.2f}.'

    # A invés de criar o Método assessor em python
    # criamos uma propriedade

    @property
    def saldo(self):
        return f'Seu Saldo é de {self.__saldo:.2f}.'

    def depositar(self, valor):
        if valor < 0:
            return print('Valor de deposito deve ser positivo.')
        self.__saldo += valor
        return print(f'Deposito de {valor:.2f}. {self.saldo}')

    def sacar(self, valor):
        if valor < 0:
            return print('Valor para saque deve ser positivo.')
        if valor > self.__saldo:
            return print(f'Saldo Insuficiente para o saque solicitado de {valor:.2f}.')
        self.__saldo -= valor
        return print(f'Saque de {valor:.2f}. {self.saldo}')


if __name__ == '__main__':
    c1 = Conta(1, 'Alex')
    print(vars(c1))
    c1.depositar(200)
    c1.depositar(300)
    print(c1.saldo)
    c1.sacar(5000)
    print(c1.saldo)
    c1.depositar(-300)
    c1.sacar(-300)
    c1.sacar(300)
