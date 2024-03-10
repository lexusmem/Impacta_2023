import requests
from pprint import pprint

# pip instal comando do python para instalação de pacotes externos
# comando para instalação de pacotes externos

# versão do pip - executar na shell
# pip --version

# Atualizar o pip - executar na shell
# -m pip install --upgrade pip

# versão do pip - executar na shell
# pip install nome_do_pacote

# bibliotecas instaladas - executar na shell
# pip list

# informações sobre a biblioteca instalada - executar na shell
# pip show nome_do_pacote

# desinstalar pacotes instaladas - executar na shell
# pip uninstall nome_do_pacote

# lista todos os pacotes Python e suas respectivas versões que estão
# instalados no seu ambiente virtual atual - executar na shell
# pip freeze

# criar arquivo txt com lista todos os pacotes Python e suas respectivas
# versões que estão instalados no seu ambiente virtual atual
# executar na shell
# pip freeze > requirements.txt

# Este arquivo pode ser usado para:
# Compartilhar as dependências do seu projeto:
# Ao compartilhar o arquivo requirements.txt, você pode garantir que outras
# pessoas que desejam executar seu projeto possam instalar as mesmas versões
# dos pacotes que você está usando.
# Recriar o ambiente virtual:
# Se você precisar reinstalar seu ambiente virtual, o arquivo requirements.txt
# pode ser usado para instalar automaticamente todos os pacotes necessários.
# Manter o controle das dependências:
# O arquivo requirements.txt serve como um registro das dependências do seu
# projeto, o que pode ser útil para rastrear quais pacotes estão sendo usados
# e para identificar possíveis problemas de compatibilidade.

# com a lista de requisitos podemos solicitar ao pip instalar todas os pacotes
# e versões que constam no arquivo txt - executar na shell
# pip install -r requirements.txt

# exemplo: - executar na shell
# pip install requests

response = requests.get('http://www.google.com')
print(response)

pprint(response.content)

pprint(dir(response))

pprint(response.json)
