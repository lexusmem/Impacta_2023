# polimorfismo sobrecarga
# mesmo método tem mais de uma forma.
# Python única forma de fazer é com número de parâmetro diferente.
# Formas diferente de executar o mesmo código:
# exemplo print
print('Alex', 1, 2)
print('Alex', 1, 2, sep='\n')

# exemplo + 'soma' que para número executa uma operação matemática,
# e para strings concatena
print(1 + 2)
print("1" + "2")


# ou exemplo, def abaixo o parâmetro é None porem ele,
# se comporta difente quando passamos o valor no atributo.
def sobrecarga(nome, numero=None):
    print(nome)
    if numero:
        print(numero)


print('Primeira execução')
sobrecarga('Alex')

print('Segunda execução')
sobrecarga('Alex', 10)

# polimorfismo de sobrescrita
# Ocorre, por exemplo, quando uma classe filha cria um mesmo método que consta
# na classe pai, nesses casos é executado o método que consta na classe filha
# sobrescrevendo o método da classe pai.
