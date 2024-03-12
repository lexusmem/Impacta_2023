# Erros e exceções

# assert

# Em Python, assert é uma construção de linguagem usada para verificar se uma
# expressão booleana é verdadeira. É similar a uma instrução if usada para
# checagem de condições, porém com algumas diferenças importantes.

# Como funciona o assert:
# Você escreve a palavra-chave assert seguida de uma expressão booleana.
# O interpretador Python avalia a expressão.
# Se a expressão for verdadeira (True), o código continua a ser executado
# normalmente. Se a expressão for falsa (False), a exceção AssertionError é
# lançada.

x = 10

assert x > 5
print('Assert True. X maior que 5.')

# assert x < 5
# O print abaixo não será executado. Será lançado um erro.
# A expressão é falsa, AssertionError é lançada
# print('Assert False. X maior que 5.')

# raise

# O raise em Python é uma construção usada para lançar exceções.
# Exceções são eventos que sinalizam erros ocorridos durante a execução do
# programa. Elas interrompem o fluxo normal do código e permitem que você lide
# com situações inesperadas.

# raise AssertionError

# A exceção AssertionError em Python é usada para indicar que uma condição
# esperada não foi atendida durante a execução do programa. É como uma
# verificação que você coloca no código para garantir que certas suposições ou
# premissas sobre o estado do programa estejam corretas.


def divide(x, y):
    if y == 0:
        raise AssertionError("Divisão por zero não é permitida!")
    return x / y

# lançamento do erro AssertionError.
# divide(10, 0)

# TypeError

# Em Python, TypeError é uma exceção padrão (built-in) que indica um erro
# relacionado a tipos de dados. Ela é lançada sempre que uma operação é
# realizada em objetos de tipos incompatíveis.


x = 10
y = "texto"
# soma = x + y
# Gera TypeError: unsupported operand type(s) for +: 'int' and 'str'


def divide_2(x, y):
    return x / y
# resultado = divide_2(" dez", 2)
# Gera TypeError: unsupported operand type(s) for /: 'str' and 'int'


lista = ["item1", "item2"]

# item = lista["um"]
# Gera TypeError: list indices must be integers or slices, not str


# o que é a função isinstance

# A função isinstance em Python é usada para verificar se um objeto é uma
# instância de uma classe ou um de seus subtipos. Em outras palavras, ela
# permite checar se um objeto pertence a uma determinada classe ou herda dela.

# A função isinstance retorna True se o objeto for uma instância da classe
# especificada ou de qualquer uma de suas subclasses, e False caso contrário.

# Exemplo:

class Animal:
    pass


class Cachorro(Animal):
    pass


classe1 = Cachorro()
classe2 = "texto"
classe3 = Animal()
print(isinstance(classe1, Cachorro))  # True
print(isinstance(classe2, Cachorro))  # False
print(isinstance(classe3, Animal))  # True
print(isinstance(classe3, Cachorro))  # True (Cachorro é subclasse de Animal)


# Utilização de isinstance, para verificar o tipo de um objeto antes de usá-lo:
def somar_numeros(x, y):
    if isinstance(x, (int, float)) and isinstance(y, (int, float)):
        return x + y
    else:
        raise TypeError("Somente números podem ser somados")


# somar_numeros('w', 10)

# Utilização de isinstance para filtrar objetos em uma lista
# com base na classe:

lista = ["cachorro", classe1, classe3]
animais = [item for item in lista if isinstance(item, Animal)]
print(animais)  # Saída: [Cachorro(), Animal()]

# Exception
# Em Python, Exception é a classe base para a hierarquia de exceções. Todas as
# exceções (errors) que você encontra ou cria em Python são subclasses (filhas)
# da classe Exception.

# criação de error:
# raise NameIsEmptyError


class NameIsEmptyError(Exception):
    pass


class Paciente:
    def __init__(self, nome):
        self.__paciente = nome
        # .... restante do código que inicia os dados do paciente.

    @property
    def paciente(self):
        return self.__paciente

    @paciente.setter
    def paciente(self, nome):
        if not isinstance(nome, str):
            raise TypeError("'nome' inválido, utilize letras.")
        if nome == '':
            raise NameIsEmptyError("'nome' é obrigatório!")
        self.__paciente = nome


if __name__ == '__main__':

    paciente_1 = input('Digite o nome do paciente:')
    alex = Paciente(paciente_1)

    print(alex.paciente)

    # testando os erro:
    # alex.paciente = ""
    # alex.paciente = 10

    alex.paciente = 'alex_2'

    print(alex.paciente)
