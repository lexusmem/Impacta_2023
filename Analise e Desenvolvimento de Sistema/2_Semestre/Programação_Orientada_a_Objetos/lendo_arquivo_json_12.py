import json
from criar_arquivo_json import caminho, cliente_str, cliente

cliente_carregado_da_string = json.loads(cliente_str)

with open(f'{caminho}cliente_arquivo_json_12.json', 'r') as f:
    cliente_carregado_do_arquivo = json.load(f)

print('Comparação 1: ', cliente_carregado_da_string ==
      cliente_carregado_do_arquivo)
print('Comparação 2: ', cliente_carregado_do_arquivo ==
      cliente_carregado_da_string)
