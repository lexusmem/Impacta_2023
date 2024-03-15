import json

caminho = '.\\Impacta_2023\\Analise e Desenvolvimento de Sistema\\2_Semestre\\Programação_Orientada_a_Objetos\\'

cliente = {
    "cliente": {
        "id": 2020,
        "nome": "Maria Aparecida"
    },
    "pagamentos": [
        {
            "id": 123,
            "descricacao": "Compra do livro Cangaceiro JavaScript",
            "valor": 50.5
        },
        {
            "id": 124,
            "descricacao": "Mensalidade escolar",
            "valor": 1500
        }
    ]
}

# método dumps com 's' escreve em uma string
cliente_str = json.dumps(cliente, indent=2)
print(cliente_str)

# método dump sem 's' escreve em um arquivo
with open(f'{caminho}cliente_arquivo_json_12.json', 'w') as f:
    json.dump(cliente, f, indent=2)
