class Mae:   # Mamifero - CLASSE MAE
    def __init__(self, atributo_mae):
        print('Executando o init da Classe Mae.')
        self.atributo_mae = atributo_mae


# Classe Filha herdando da classe Mae
# Quando criar uma classe que deve conter o seu próprio atributo e deve
# herdar atributos de outra classe deve incluir manualmente os atributos
# através da classe super()
class Filha (Mae):    # Felino
    def __init__(self, atributo_filha, atributo_mae):
        print('Executando o init da Classe Filha.')
        self.atributo_filha = atributo_filha
        super().__init__(atributo_mae)


# Classe Filha herdando da classe Mae e Filha
# Quando criar uma classe que deve conter o seu próprio atributo e deve
# herdar atributos de outra classe deve incluir manualmente os atributos
# através da classe super()
class Neta (Filha):  # Gato
    def __init__(self, atributo_neta, atributo_filha, atributo_mae):
        print('Executando o init da Classe Neta.')
        self.atributo_neta = atributo_neta
        super().__init__(atributo_filha, atributo_mae)

# Exemplo de criação de classe herdando de classe interna do python
# class MeusInteiros(int):
#     def metodo_extra(self):
#         pass


if __name__ == '__main__':
    print('\nCirando objeto de Mae...')
    mae = Mae('Atributo Mae')
    print('Mostrando os objetos da classe Mae')
    print(vars(mae))

    print('\nCirando objeto de Filha...')
    filha = Filha('Atributo Filha', 'Atributo Mae')
    print('Mostrando os objetos da classe Filha')
    print(vars(filha))

    print('\nCirando objeto de Neta...')
    neta = Neta('Atributo Neta', 'Atributo Filha', 'Atributo Mae')
    print('Mostrando os objetos da classe Neta')
    print(vars(neta))

    print('\n\n\n')
    print(mae)
    print(type(mae))
    print(filha)
    print(type(filha))
    print(neta)
    print(type(neta))

    # verificar se um objeto é uma instancia de uma determinada classe
    # função isinstance verificar se é um objeto de uma classe
    print(isinstance(mae, Filha))
    print(isinstance(mae, Mae))
    print(isinstance(filha, Mae))
    print(isinstance(filha, Neta))
    print(isinstance(neta, Mae))
