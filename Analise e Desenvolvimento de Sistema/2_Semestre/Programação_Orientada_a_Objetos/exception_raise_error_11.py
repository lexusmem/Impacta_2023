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
