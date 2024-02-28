class Passaro:
    def __init__(self, vida, ataque, defesa):
        # atributos
        self.vida = vida
        self.ataque = ataque
        self.defesa = defesa

    # métodos
    def atacar(self, alvo):
        self.alvo = alvo
        print('teste método atacar.....')

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
        print('teste método nadar.....')


class PassaroDeCompanhia(PassaroAereo):
    # Atributos herdados da classe filha PassaroAereo
    def __init__(self, companheiro, vida, ataque, defesa):
        # Atributos
        self.companheiro = companheiro
        # super() - função super permite acessar e reutilizar métodos __init__
        # de classes ancestrais.
        super().__init__(vida, ataque, defesa)


class Pinguim(PassaroAquatico):
    def __init__(self, peso, vida, ataque, defesa):
        # Atributos
        self.peso = peso
        # super() - função super permite acessar e reutilizar métodos __init__
        # de classes ancestrais.
        super().__init__(vida, ataque, defesa)


if __name__ == '__main__':
    aguia = PassaroDeCompanhia('Alex', 100, 300, 250)
    pinguim = Pinguim(5, 140, 80, 400)
    print(vars(aguia))
    print(vars(pinguim))
    print('Fim')
    teste = PassaroAquatico(100, 200, 50)
    print(vars(teste))
    teste.nadar()
    teste.atacar('teste')
