# def troca(s, i, j):
#     s[i], s[j] = s[j], s[i]


# def empura_minimo(s, n):
#     for i in range(n-1):
#         if s[i] < s[i+1]:
#             troca(s, i, i+1)


# def empura_maximo(s, n):
#     for i in range(n-1):
#         if s[i] > s[i+1]:
#             troca(s, i, i+1)


# def bubble_sort(s, crescente=False):
#     n = len(s)

#     if crescente:
#         empurra = empura_maximo
#     else:
#         empurra = empura_minimo

#     while n > 1:
#         empurra(s, n)
#         n -= 1


# valor = [48, 5, 39, 56, 40, 52]

# bubble_sort(valor, False)

# print(valor)

n = int(input('Digite um número: '))

inicio = 0
fim = n
passo = -1

for i in range(inicio, fim):
    print(i, end=' ')

print()

for i in range(fim - 1, inicio - 1, passo):
    print(i, end=' ')
