import requests
import pprint

APIKEY = '6a2345fe'


def busca_por_texto(texto_busca):
    url = f'https://www.omdbapi.com/?s={texto_busca}&apikey={APIKEY}'
    pedido = requests.get(url)
    dicionario_do_pedido = pedido.json()
    return dicionario_do_pedido


def busca_por_id(id_busca):
    url = f'https://www.omdbapi.com/?i={id_busca}&apikey={APIKEY}'
    pedido = requests.get(url)
    dicionario_do_pedido = pedido.json()
    return dicionario_do_pedido


def busca_por_titulo(titulo_busca):
    url = f'https://www.omdbapi.com/?t={titulo_busca}&apikey={APIKEY}'
    pedido = requests.get(url)
    dicionario_do_pedido = pedido.json()
    return dicionario_do_pedido


def busca_qtd_total(texto_buscar):
    busca = busca_por_texto(texto_buscar)
    return int(busca['totalResults'])


def busca_qtd_por_tipo(texto_busca):
    tipo_busca = int(input('''
        [1] - Movie
        [2] - Game
        [3] - Series
        [4] - Episode

        Digite o n° do tipo de busca desejado: '''))

    if tipo_busca == 1:
        tipo = 'movie'
    elif tipo_busca == 2:
        tipo = 'game'
    elif tipo_busca == 3:
        tipo = 'series'
    elif tipo_busca == 4:
        tipo = 'episode'

    url = f'https://www.omdbapi.com/?s={
        texto_busca}&apikey={APIKEY}&type={tipo}'
    pedido = requests.get(url)
    dicionario_do_pedido = pedido.json()
    return int(dicionario_do_pedido['totalResults'])


def nome_filme_por_id(id):
    busca = busca_por_id(id)
    print(f'Id buscada: {id}.')
    return busca['Title']


def ano_lancamento_filme_por_id(id):
    busca = busca_por_id(id)
    print(f'Id buscada: {id}.')
    return busca['Year']


def dados_dos_filmes_por_id(id):
    dados = busca_por_id(id)
    dict_pt = {}
    dict_pt['ano'] = dados['Year']
    dict_pt['nome'] = dados['Title']
    dict_pt['diretor'] = dados['Director']
    dict_pt['genero'] = dados['Genre']
    return dict_pt


# print('\n===============BUSCA POR TEXTO===============')
# busca_texto = busca_por_texto('star wars')
# pprint.pprint(busca_texto)
# print(f'Total de Resultados: {busca_texto['totalResults']}.')
# pprint.pprint(busca_texto['Search'][0])

# print('\n===============BUSCA POR TITULO===============')
# busca_titulo = busca_por_titulo('dune')
# pprint.pprint(busca_titulo)

# print('\n===============BUSCA POR ID===============')
# busca_id = busca_por_id('tt1160419')
# pprint.pprint(busca_id)

# print('\n===============QUANTIDADE DE RETORNOS DA BUSCA POR TEXTO===============')
# busca_qtd = busca_qtd_total('star wars')
# print(busca_qtd)

# print('\n===============QUANTIDADE DE RETORNOS DA BUSCA POR TEXTO POR TIPO===============')
# qtd_filmes = busca_qtd_por_tipo('star wars')
# print(qtd_filmes)

# print('\n===============NOME DO FILME POR ID===============')
# nome_filme_id = nome_filme_por_id('tt0076759')
# print(nome_filme_id)

# print('\n===============ANO LANÇAMENTO DO FILME POR ID===============')
# ano_lancamento_filme = ano_lancamento_filme_por_id('tt0076759')
# print(ano_lancamento_filme)

# print('\n===============DADOS DO FILME POR ID===============')
# dados_dos_filmes = dados_dos_filmes_por_id('tt0076759')
# pprint.pprint(dados_dos_filmes)


def busca_dez_filmes(texto_busca):
    busca = busca_por_texto(texto_busca)
    x = 0
    lista = []
    while x < 10:
        filme = {}
        filme['nome'] = busca['Search'][x]['Title']
        filme['ano'] = busca['Search'][x]['Year']
        lista.append(filme)
        x += 1
    return lista


teste = busca_dez_filmes('battleship')
pprint.pprint(teste)
