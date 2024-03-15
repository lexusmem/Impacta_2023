import csv

caminho = '.\\Impacta_2023\\Analise e Desenvolvimento de Sistema\\2_Semestre\\Programação_Orientada_a_Objetos\\'

with open(f'{caminho}estoque.csv', 'r', newline='', encoding='utf-8') as arquivo_csv:
    leitor = csv.reader(arquivo_csv, delimiter=';')
    novo_estoque = []
    for linha in leitor:
        novo_estoque.append(linha)

print(len(novo_estoque))

for x in range(len(novo_estoque)):
    print(novo_estoque[x])


x = 0
while x < len(novo_estoque):
    print(novo_estoque[x])
    x += 1
