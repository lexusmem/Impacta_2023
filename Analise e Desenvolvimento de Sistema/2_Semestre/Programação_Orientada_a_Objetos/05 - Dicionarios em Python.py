# Dicionários
# Estrutura de chave e valor
# cada chave é única

notas = {'Jack': 6.0, 'Alex': 10.0, 'Ana': 7.5}

pessoas = {
    'Nome': 'Alex',
    'Cor Favorita': 'Azul',
    'idade': 37,
    'telefone': '(11) 96176 1340',
    'e-mail': 'alexsisousa@gmail.com'
}
print(notas)
print(notas['Alex'])
print(pessoas)

notas['Andre'] = 9.5

print(notas)
print(notas.keys())
print(notas.values())
print(notas.items())

notas['Andre'] += .5

print(notas)
print(notas['Andre'])

notas.update({'Laura': 7.5})
print(notas)

notas.update({"Alex": 0})
print(notas)

for itens in notas.items():
    print(itens)

for chaves in notas.keys():
    print(chaves)

for valores in notas.values():
    print(valores)

for nome, nota in notas.items():
    print(f'{nome} tirou nota {nota}')
