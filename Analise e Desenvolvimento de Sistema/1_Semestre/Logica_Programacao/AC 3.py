# x = 100
# y = 200
# i = 0
# bom_dia = 0
# boa_tarde = 0

# while i < x:
#     print(f"bom dia {bom_dia}")
#     i += 1
#     bom_dia += 1
#     j = 0
#     while j < y:
#         print(f"boa tarde {boa_tarde}")
#         j += 1
#         boa_tarde += 1
# print('Boa Noite')
# print(f"bom dia {bom_dia}")
# print(f'Boa tarde {boa_tarde}')

# def misterio(x, v, n):
#     i = 0
#     while i < n and v[i] != x:
#         i += 1
#     if i < n:
#         return i
#     else:
#         return -1


# a = ['b', 'x', 'd', 'v', 'e', 'r', 'e', 'p']

# r1 = misterio('e', a, 8)
# r2 = misterio('z', a, 8)
# r3 = misterio('v', a, 3)

# print(r1, r2, r3)

# def enigma(v, n):
#     i = 0
#     while i < n:
#         v[i] = 2 * v[i]
#         i += 2
#     return


# def exibe(v, n):
#     i = 0
#     while i < n:
#         print(v[i], end=' ')
#         i += 1
#     return


# v = [10, 20, 30, 40, 50]

# enigma(v, len(v))
# exibe(v, len(v))

# def bubble_sort(v, n):

#     exibe(v, n)
#     tam = n

#     while tam > 1:
#         empurra(v, tam)
#         exibe(v, tam)
#         tam -= 1

#     exibe(v, n)

#     return


# def empurra(v, n):
#     i = 0

#     while i < n-1:
#         if v[i] > v[i+1]:
#             troca(v, i, i+1)
#         i += 1
#     return


# def troca(v, i, j):
#     temp = v[i]
#     v[i] = v[j]
#     v[j] = temp
#     return


# def exibe(v, n):
#     i = 0
#     while i < n:
#         print(v[i], end=' ')
#         i += 1
#     print()
#     return


# a = bubble_sort([40, 20, 50, 30, 10], 5)

# v = [10, 20, 30, 40, 50]
# print(v[-1])

i = 10
while i >= 0:
    print(i)
    i -= 1
print('Fogo')
