class Passaro:
    def __init__(self, vida, ataque, defesa):
        # atributos
        self.vida = vida
        self.ataque = ataque
        self.defesa = defesa

    # métodos
    def atacar(self, alvo):
        pass

    def fugir(self, destino):
        pass


# Inclusão de duas subclasses de Pássaros
# Classes que irão herdar de Pássaros
class PassaroAereo(Passaro):
    # classes sem atributos novos
    # método
    def voar(self):
        pass


class PassaroAquatico(Passaro):
    # classes sem atributos novos
    # método
    def nadar(self):
        pass


class PassaroDeCompanhia(PassaroAereo):
    def __init__(self, companheiro, vida, ataque, defesa):
        # Atributos
        self.companheiro = companheiro
        super().__init__(vida, ataque, defesa)


class Pinguim(PassaroAquatico):
    def __init__(self, peso, vida, ataque, defesa):
        # Atributos
        self.peso = peso
        super().__init__(vida, ataque, defesa)


if __name__ == '__main__':
    aguia = PassaroDeCompanhia('Alex', 100, 300, 250)
    pinguim = Pinguim(5, 140, 80, 400)
    print(vars(aguia))
    print(vars(pinguim))
    print('Fim')
