# Algorítimo Bubble sort.

def ordenar(lista):
    tamanho_1 = len(lista)
    item_1 = 0

    while item_1 < tamanho_1:
        tamanho = len(lista)
        item = 0
        while item < tamanho-1:
            if lista[item] > lista[item+1]:
                temp = lista[item + 1]
                lista[item + 1] = lista[item]
                lista[item] = temp
            item += 1
        item_1 += 1
    print(lista)


lista = [55, 64, 23, 12, 0, 4, 3998, 3476, 39762, 234, 4573]
ordenar(lista)
