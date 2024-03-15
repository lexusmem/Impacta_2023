import csv

caminho = '.\\Impacta_2023\\Analise e Desenvolvimento de Sistema\\2_Semestre\\Programação_Orientada_a_Objetos\\'

colunas = [
    'Descrição',
    'Potencia',
    'Tensão',
    'Qtd Estoque',
    'Preço'
]

estoque = [
    ['liquidificador', 800, 220, 5, 210],
    ['liquidificador', 800, 220, 5, 210],
    ['liquidificador', 800, 220, 5, 210],
]

with open(f'{caminho}estoque.csv', 'w', newline='', encoding='utf-8') as arquivo_csv:
    escritor = csv.writer(arquivo_csv, delimiter=';')
    escritor.writerow(colunas)
    escritor.writerows(estoque)
