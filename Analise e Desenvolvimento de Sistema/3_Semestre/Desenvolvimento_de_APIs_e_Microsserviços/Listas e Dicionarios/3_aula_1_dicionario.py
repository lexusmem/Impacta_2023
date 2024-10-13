# criar dicionario
agenda = {}
print(agenda)
print(type(agenda))

# inserir elementos no dicionario chave e valor
agenda['maria'] = 9982223322
agenda['alex'] = 961761340
agenda['pamela'] = 9614585458
agenda['chave'] = 'valor'
print(agenda)

# consulta basta informar a chave
print(agenda['alex'])

# verificar se uma chave existe na lista
print('alex' in agenda)
print('laura' in agenda)
print('pamela' in agenda.keys())
chaves_dicionario = list(agenda.keys())
print(chaves_dicionario)
print(chaves_dicionario[3])
for chaves in chaves_dicionario:
    print(chaves)

# se quiser verificar o valor
print(961761340 in agenda.values())
valores_dicionario = list(agenda.values())
print(valores_dicionario)
print(valores_dicionario[3])
for valores in valores_dicionario:
    print(valores)
