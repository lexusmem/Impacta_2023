lista = 5


# crescente [1 ... lista]
# decrescente [lista ... 1]

# Certo
# for i in range(lista, 0, -1):
#     print(i)
#     resultado = 5,4,3,2,1

# Errado
# for i in range(0, lista+1):
#     print(i)
#     resultado = 0,1,2,3,4,5

# Errado
# for i in range(0, lista+1, 1):
#     print(i)
#     resultado = 0,1,2,3,4,5

# Errado
# for i in range(0, lista):
#     print(i)
#     resultado = 0,1,2,3,4

# Errado
# for i in range(lista, -1, -1):
#     print(i)
#     resultado = 5,4,3,2,1,0

# Errado
# for i in range(1, lista, 1):
#     print(i)
#     resultado = 1,2,3,4


# Errado
# for i in range(lista, 1, -1):
#     print(i)
#     resultado = 5,4,3,2

# ERRADO
# def conta_centro(matriz):
#     soma = 0
#     l = len(matriz)
#     c = len(matriz[0])
#     for i in range(1, l):
#         for j in range(1, c):
#             soma += matriz[i][j]
#     return soma

# CERTO
# def conta_centro(matriz):
#     soma = 0
#     l = len(matriz)
#     c = len(matriz[0])
#     for i in range(1, l - 1):
#         for j in range(1, c - 1):
#             soma += matriz[i][j]
#     return soma


# ERRADO
# def conta_centro_1(matriz):
#     soma = 0
#     l = len(matriz)
#     c = len(matriz[0])
#     for i in range(2, l - 1):
#         for j in range(2, c - 1):
#             soma += matriz[i][j]
#     return soma


# matriz = [[50, 50, 50, 50, 50, 50, 50],
#           [50, 1, 1, 1, 1, 1, 50],
#           [50, 1, 1, 1, 1, 1, 50],
#           [50, 1, 1, 1, 1, 1, 50],
#           [50, 50, 50, 50, 50, 50, 50]
#           ]

# print(conta_centro(matriz))
# print(conta_centro_1(matriz))


v = 1
s = [1, 1, 1, 1, 1, 2, 1]


def localizar(v, s):
    indice = []
    for i, item in enumerate(s):
        if item == v:
            indice.append(i)
    return indice


print(localizar(v, s))
