import sys
from pprint import pprint

# ambiente virtual venv
# na pasta raiz (pasta em que vai inserir um ambiente virtual) executar o
# comando no shell:
# py -m venv nome_do_ambiente_virtual_desejado

# Normalmente cria-se o ambiente virtual com nome venv
# py -m venv venv

# ou o nome do ambiente virtual com "." na frente para a pasta ser criada
# oculta
# py -m venv .venv

# sys.path para mostrar onde esta sendo executado.
# pprint biblioteca que imprime de forma diferente
pprint(sys.path)
