import requests

nome = input("Digite o nome: ")
sexo = input("Digite o sexo: ")
cabelo = input("Digite a cor do cabelo: ")

dados = {"nome": nome, "sexo": sexo, "cabelo": cabelo}

x = requests.post("http://127.0.0.1:5000/pessoa", json=dados)
if x.status_code != 200:
    print(f"[{x.status_code}] {x.text}")
else:
    print(x.text)
