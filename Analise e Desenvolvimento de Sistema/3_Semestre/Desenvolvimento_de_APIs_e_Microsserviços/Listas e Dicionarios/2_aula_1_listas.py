#  para criar uma lista vazia
lista = []
print(lista)
print(type(lista))

# para inserir elementos
lista.append('banana')
lista.append('melancia')
lista.append('morango')
print(lista)

# é possivel criar lista já com elementos
lista = ['gato', 'cachorro', 'peixe']
print(lista)

# acessar elementos através dos números
print(lista[0])
print(lista[2])

# verificar se um elementos esta na lista
elemento = 'peixe' in lista
print(elemento)
