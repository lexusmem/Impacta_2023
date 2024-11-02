import requests


def construtor_pessoa():
    nome = input("Digite o nome: ")
    sexo = input("Digite o sexo: ")
    cabelo = input("Digite a cor do cabelo: ")
    dados = {"nome": nome, "sexo": sexo, "cabelo": cabelo}
    return dados


qtd_pessoas_cadastro = int(
    input('Informe o número de pessoas para cadastro: '))
num = 0

while num < qtd_pessoas_cadastro:
    x = requests.post("http://127.0.0.1:5000/pessoa", json=construtor_pessoa())
    if x.status_code != 200:
        print(f"[{x.status_code}] {x.text}")
    else:
        print(x.text)
    num += 1

print('=== Alteração ===')
id_alteracao = input('Informe o Id da Pessoa para Alteração: ')

x = requests.put(
    f"http://127.0.0.1:5000/pessoa/{id_alteracao}", json=construtor_pessoa())
if x.status_code != 200:
    print(f"[{x.status_code}] {x.text}")
else:
    print(x.text)

id_consulta = input('Informe o Id da Pessoa para Consulta: ')

x = requests.get(f"http://127.0.0.1:5000/pessoa/{id_consulta}")
if x.status_code != 200:
    print(f"[{x.status_code}] {x.text}")
else:
    print(x.text)

id_deletar = input('Informe o Id da Pessoa para Deletar: ')

x = requests.delete(f"http://127.0.0.1:5000/pessoa/{id_deletar}")
if x.status_code != 200:
    print(f"[{x.status_code}] {x.text}")
else:
    print(x.text)
