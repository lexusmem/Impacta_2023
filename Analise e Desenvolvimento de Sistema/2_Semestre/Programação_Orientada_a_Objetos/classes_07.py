# Abstração - representar algo do mundo real com suas características
# (atributos) e seu comportamento (métodos).
# Criação da classe Livro
class Livro:
    def __init__(self, nome, autor):
        # Criação dos atributos (características):
        self.nome = nome
        self.autor = autor
        self.editora = 'Editora Novo Mundo'

    # Criação de métodos:

    def identidade(self):
        return (f'Sou o livro {self.nome} e estou salvo no endereço de '
                f'memória: {id(self)}')


if __name__ == '__main__':
    # Instanciando o objeto a partir da classe Livro()
    livro_1 = Livro('FactFulness', 'Hans Rosling')

    # função vars - diz quais os atributos do objeto
    print(f'Atributos do Livro 1: {vars(livro_1)}')

    # Impressão dos atributos instanciados no objeto livro_1
    print(livro_1.nome)
    print(livro_1.autor)
    print(livro_1.editora)
    print(livro_1.identidade())
    print(id(livro_1))

    print('\n')
    livro_2 = Livro('Pense & Enriqueça', 'Napoleon Hill')
    print(f'Atributos do Livro 2: {vars(livro_2)}')
    print(livro_2.nome)
    print(livro_2.autor)
    print(livro_2.editora)
    print(livro_2.identidade())
    print(id(livro_2))
