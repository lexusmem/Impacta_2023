class ContaBancaria():
    def __init__(self, numero, titular):
        self.numero = numero
        self.titular = titular
        self.__saldo = 0

    @property
    def saldo(self):
        return self.__saldo

    def depositar(self, valor):
        if valor < 0:
            print('Valor deposito inválido, o valor deve ser positivo.')
            return
        self.__saldo += valor
        print(f'Deposito realizado R$ '
              f'{valor:.2f}. Saldo: R$ {self.__saldo:.2f}.')

    def sacar(self, valor):
        if valor < 0:
            print('Valor saque inválido, o valor deve ser positivo.')
            return 0
        if valor > self.__saldo:
            print(f'Saldo Insuficiente. Saldo R$ {self.__saldo:.2f}.')
            return 0
        self.__saldo -= valor
        print('Realizando saque...')
        print(f'Saque Realizado R$ {valor:.2f}. Saldo R$ {self.__saldo:.2f}.')
        return valor


class ContaPoupanca(ContaBancaria):
    def __init__(self, numero, titular):
        self.rendimento = 0.5
        super().__init__(numero, titular)

    def aplicar_rendimento(self):
        rendimento = self.saldo * self.rendimento
        super().depositar(rendimento)
        return rendimento


class ContaInvestimento(ContaBancaria):
    def __init__(self, numero, titular, gerente):
        self.gerente = gerente
        super().__init__(numero, titular)

    def sacar(self, valor):
        print('Verificando prazo de investimento')
        print('Calculando impostos e taxas...')
        return super().sacar(valor)


if __name__ == '__main__':
    c_poupanca = ContaPoupanca(numero=1, titular='Alex')
    print(vars(c_poupanca))
    c_poupanca.depositar(100)
    c_poupanca.sacar(50)
    print(f'Rendimento aplicado R$ {c_poupanca.aplicar_rendimento():.2f}')
    print(f'R$ {c_poupanca.saldo:.2f}')

    print('\n')
    c_investimento = ContaInvestimento(2, 'Alex', 'Laura')
    print(vars(c_investimento))
    c_investimento.depositar(100)
    c_investimento.sacar(50)
    print(f'R$ {c_investimento.saldo:.2f}')
