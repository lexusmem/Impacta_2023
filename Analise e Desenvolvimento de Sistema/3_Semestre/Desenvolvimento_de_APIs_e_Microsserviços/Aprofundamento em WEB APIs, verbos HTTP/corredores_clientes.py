from httpx import delete
import requests
import pprint


def todos_corredores():
    url = 'http://127.0.0.1:5000/corredores'
    dados = requests.get(url)
    lista = dados.json()
    return lista


corredores = todos_corredores()
pprint.pprint(corredores)


def adiciona_corredor(nome, tempo, id):
    url = 'http://127.0.0.1:5000/corredores'
    dici_corredor = {'nome': nome, 'tempo': tempo, 'id': id}
    dados = requests.post(url, json=dici_corredor)
    return True


# adiciona_corredor('Alex Sousa', 23.50, 37)
# corredores = todos_corredores()
# pprint.pprint(corredores)


def maior_tempo():
    url = 'http://127.0.0.1:5000/corredores/maior_tempo'
    dados = requests.get(url)
    lista = dados.json()
    return lista['nome']


# mais_lento = maior_tempo()
# print(mais_lento)


def deleta_maior_tempo():
    url = 'http://127.0.0.1:5000/corredores/maior_tempo'
    dados = requests.delete(url)
    if dados.status_code == 500:
        return 'Não possui corredor para deletar!'
    else:
        return 'Deletado'


# excluir_mais_lento = deleta_maior_tempo()
# pprint.pprint(corredores)
# print(excluir_mais_lento)
# pprint.pprint(corredores)

'''
O VERBO DELETE DEVERIA SER IDEMPOTENTE.
DEVERIA SER O CASO QUE A SEGUNDA CHAMADA NÃO CAUSA NOVO EFEITO COLATERAL
'''


def id_corredores(id):
    url = f'http://127.0.0.1:5000/corredores/{id}'
    dados = requests.get(url)
    lista = dados.json()
    if dados.status_code == 404:
        return 'Corredor não localizado.'
    else:
        nome = lista['corredor']['nome']
        tempo = lista['corredor']['tempo']
        return (nome, tempo)


alex = id_corredores(14)
print(alex)
print(type(alex))


def deletar_por_id_corredores(id):
    url = f'http://127.0.0.1:5000/corredores/{id}'
    dados = requests.delete(url)
    if dados.status_code == 404:
        return 'Corredor não localizado.'
    return "Ok Excluído"


# alex_1 = deletar_por_id_corredores(37)
# print(alex_1)

# pprint.pprint(corredores)

def novo_tempo_corredores(id, tempo_enviado):
    url = f'http://127.0.0.1:5000/corredores/{id}'
    dados = requests.put(url, json={'tempo': tempo_enviado})
    if dados.status_code == 400:
        return 'Tempo não atualizado por ser maior que o anterior.'
    if dados.status_code == 404:
        return 'Corredor não encontrado'
    return "Atualizado"


print(novo_tempo_corredores(20, 21.5))

pprint.pprint(corredores)
