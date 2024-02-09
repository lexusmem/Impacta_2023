# sequencias

# listas
# pode existir diversos tipos de dados.
# mutável

print('LISTAS - LIST')
print("="*40)
lista_inteiros = [1, 2, 3]
lista_string = ['a', 'b', 'c']
lista_mista = [1, 'a', lista_inteiros, lista_string]
cria_lista = list('abc')
print(lista_mista)
print(lista_mista[2])
print(lista_mista[2][1])
print(len(lista_inteiros))
print(lista_inteiros[0])
print(cria_lista)
cria_lista.append('alex')
print(cria_lista)

# tuplas
# Tuplas são imutáveis
print('\nTUPLAS - TUPLE')
print("="*40)
tupla = (1, 2, 3)
tupla_string = ('a', 'b', 'c')
tupla_mista = (1, 'a', lista_inteiros, lista_string)
tupla_com_um_item = (1,)
cria_tupla = tuple([1, 2, 3])
print(tupla)
print(tupla_string)
print(tupla_mista)
print(tupla_com_um_item)
print(cria_tupla)


# intervalos

print('\nINTERVALOS - RANGE')
print("="*40)

# Criação de range apenas com o range(FIM)
# cria intervalo de 0 a 9 - 10 posições
# na criação do intervalo o último número que será criado
# é 1 menos o número informado no range
print(range(10))
lista_range_fim = list(range(10))
print(lista_range_fim)

# Criação de range com o range(inicio, fim)
# cria intervalo de 10 a 14 - 5 posições
# na criação do intervalo o último número que será criado
# é 1 menos o número informado no range
print(range(10, 15))
lista_range_inicio_fim = list(range(10, 15))
print(lista_range_inicio_fim)

# Criação de range com o range(inicio, fim, passos)
# cria intervalo de 10 a 21 com passo de 2 - 6 posições
# na criação do intervalo o último número que será criado
# é 1 menos o número informado no range
print(range(10, 21, 2))
lista_range_inicio_fim_passos = list(range(10, 21, 2))
print(lista_range_inicio_fim_passos)
# para inverter colocar o passo negativo
lista_range_inicio_fim_passos_negativos = list(range(20, 9, -2))
print(lista_range_inicio_fim_passos_negativos)

# podemos usar o len para contar o tamanho de uma list ou tuple
# para saber o tamanho, isso é importante para percorrer dentro
# dos dados de cada lista ou tupla
print(range(len(lista_mista[2])))

# operações de pertencimento

print('\nPERTENCIMENTOS')
print("="*40)
print(lista_mista)
print('1 in lista_mista')
print(1 in lista_mista)
print('2 in lista_mista')
print(2 in lista_mista)
print('2 in lista_mista[2]')
print(2 in lista_mista[2])
print('[1, 2, 3] in lista_mista')
print([1, 2, 3] in lista_mista)
print('2 not in lista_mista')
print(2 not in lista_mista)

# desempacotamento

print('\nDESEMPACOTAMENTO')
print("="*40)
lista_desempacotamento = (list(range(1, 6)))
print(lista_desempacotamento)
a, b, c, d, e = lista_desempacotamento
print(a)
print(b)
print(c)
print(d)
print(e)
print(lista_desempacotamento)
print(*lista_desempacotamento)
print(lista_desempacotamento[0], lista_desempacotamento[1],
      lista_desempacotamento[2], lista_desempacotamento[3],
      lista_desempacotamento[4])


def teste_desempacota(a, b, c, d, e):
    print(f'{a=}, {b=}')
    print(f'{c=}, {d=}')
    print(f'{e=}')


teste_desempacota(*lista_desempacotamento)
