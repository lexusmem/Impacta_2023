import pprint


dic = {
    "alimentos": {
        "pizzas": ["margueritta", "mussarella",
                   "frango com catupiry", "portuguesa"],
        "bolos": ("floresta negra",
                  "red velvet",
                  "de laranja", "dá vó"),
        "calorias": {
            "leite": 129, "fatia pizza": 320,
            "agua": 0, "maça": 95
        }
    },
    "linguagens": [
        {"nome": "javascript", "criacao": 1996,
         "paradigma": ["eventos", "funcional"]},
        {"nome": "python", "criacao": 1991,
         "paradigma": ["orientada a objetos", "estruturada"]},
        {"nome": "haskell", "criacao": 1990,
         "paradigma": ["funcional"]}
    ]
}
# quantas chaves tem o dic
print('=================Resposta Pergunta 1=================')
print(dic.keys())
qtd_dic = len(dic.keys())
print(f'O dicionario "dic" possui {qtd_dic} chaves "{
      list(dic.keys())[0]}" e "{list(dic.keys())[1]}".')

# dic [linguagens] é uma tupla, dicionario ou lista
print('=================Resposta Pergunta 2=================')
print(type(dic["linguagens"]))
pprint.pprint(dic["linguagens"])
print(dic["linguagens"][0])

# como faço para acessar todos os bolos
print('=================Resposta Pergunta 3=================')
pprint.pprint(dic["alimentos"])
print(dic['alimentos'].keys())
print(dic["alimentos"]['bolos'])

# qual tipo da lista de todos bolos
print('=================Resposta Pergunta 4=================')
print(type(dic["alimentos"]['bolos']))

# acesse o ano de criação da linguagem javascript
print('=================Resposta Pergunta 5=================')
print(dic.keys())
print(dic['linguagens'])
print(type(dic['linguagens']))
print(dic['linguagens'][0])
print(type(dic['linguagens'][0]))
print(dic['linguagens'][0]['criacao'])

# posição 2 dic linguagens é igual a 'haskell'
print('=================Resposta Pergunta 6=================')
print(dic['linguagens'][2]['nome'] == 'haskell')

# posição 2 dic alimentos / pizza é igual a 'mussarela'
print('=================Resposta Pergunta 7=================')
print(dic["alimentos"]['pizzas'][2] == 'mussarela')
print(dic["alimentos"]['pizzas'][1] == 'mussarella')

# verificar se consta values no dicionario
print('=================Resposta Pergunta 8=================')
print(dic['linguagens'][0])
print(1996 in dic['linguagens'][0])
print(1996 in dic['linguagens'][0].values())

# verificar se consta keys no dicionario
print('=================Resposta Pergunta 9=================')
print(dic['linguagens'][0])
print('cricao' in dic['linguagens'][0])
print('criacao' in dic['linguagens'][0].keys())

# verificar se consta pudim como sobremesa
print('=================Resposta Pergunta 10=================')
print(dic["alimentos"].keys())
print(dic['alimentos']['bolos'])


# função para verificar a linguagem mais velha
print('=================Resposta Pergunta 11=================')


def mais_velha(dicionario, chave):

    if chave in dicionario:
        lista_linguagens = dicionario[chave]
        linguagem_mais_velha = lista_linguagens[0]
        for lista in lista_linguagens:
            if lista['criacao'] < linguagem_mais_velha['criacao']:
                linguagem_mais_velha = lista
        return linguagem_mais_velha
    else:
        return 'Não existe a chave informada no dicionario'


retorno = mais_velha(dic, 'linguagens')
print(retorno)

# Escreva uma função que retorno uma lista de paradigmas sem repetição
print('=================Resposta Pergunta 12=================')


def lista_paradgmas(dicionario, chave):

    lista_retorno = []

    if chave in dicionario:
        lista_linguagens = dicionario[chave]
        for lista in lista_linguagens:
            for paradgma in lista['paradigma']:
                if paradgma not in lista_retorno:
                    lista_retorno.append(paradgma)
        return lista_retorno
    else:
        return 'Não existe a chave informada no dicionario'


retorno_2 = lista_paradgmas(dic, 'linguagens')
print(retorno_2)
