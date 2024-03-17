from abc import ABC, abstractmethod

# Classe abstrata


class Funcionarios(ABC):
    @abstractmethod
    def salario(self):
        pass

    # ciando proporty abstrata
    @property
    @abstractmethod
    def nome(self):
        return self.__nome


class Vendedor(Funcionarios):
    def salario(self):
        return 'calculo 1'


class Estagiario(Funcionarios):
    def salario(self):
        return 'calculo 2'


class Programador(Funcionarios):
    def salario(self):
        return 'calculo 3'
