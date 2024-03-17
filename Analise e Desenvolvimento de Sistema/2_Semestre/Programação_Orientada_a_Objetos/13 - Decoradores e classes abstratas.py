# funções - como parâmetro e retorno de valores

# A função abaixo funciona porém ficaria gigante para converter todo tipo
# disponíveis no python

def converte(tipo, sequencia):
    convertidos = []
    if tipo == 'string':
        for item in sequencia:
            convertidos.append(str(item))
    elif tipo == 'int':
        for item in sequencia:
            convertidos.append(int(item))
    elif tipo == 'float':
        for item in sequencia:
            convertidos.append(float(item))
    else:
        raise Exception('Tipo não reconhecido. Tipos suportados\
                         "string", "int" e "float".')

    return convertidos


lista = [1, 2, 3]
print(converte('string', lista))
lista = 'Alex Sousa'
print(converte('string', lista))

# O correto seria permitir o python executar automaticamente a conversão
# passando o a função para a função


def converte_2(f, sequencia):
    convertidos = []
    for item in sequencia:
        convertidos.append(f(item))
    return convertidos


lista_1 = [0, 1, 2, 32]
print(converte_2(bool, lista_1))
lista_2 = 'Alex Sousa'
print(converte_2(bool, lista_2))

# é possível passar até uma função criada para utilizar na função converte_2.


def dobro(x):
    return x * 2


def triplo(x):
    return x*3


dobrar = converte_2(dobro, lista_1)
triplicar = converte_2(triplo, lista_2)

print(dobrar)
print(triplicar)

# FUNÇÃO MAP

# a função converte_2 criada acima não precisa ser criada
# no python existe a função map que executa a mesma tarefa

dobrar_2 = map(dobro, lista_1)
# a função map retorna um objeto map.
print(dobrar_2)
# para visualizar deve alterar o valor map retornado como por exemplo para uma
# lista.
print(list(dobrar_2))

# é possível retornar uma função também.


def teste():
    def funcao_interna():
        return 'olá mundo!'
    return funcao_interna


r = teste()
print(r)
print(r())

print(converte(tipo='string', sequencia=lista))
