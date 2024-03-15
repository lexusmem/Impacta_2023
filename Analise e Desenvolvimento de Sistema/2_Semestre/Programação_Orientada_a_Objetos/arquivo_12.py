caminho = '.\\Impacta_2023\\Analise e Desenvolvimento de Sistema\\2_Semestre\\Programação_Orientada_a_Objetos\\'

texto = 'Escrevendo e Manipulando aquivos de texto com python.'
with open(f'{caminho}arquivo_teste_1_12.txt', 'w') as f:
    f.write(texto)
s = [
    'Linha 1',
    'Linha 2',
    'Linha 3',
    'Linha 4'
]
with open(f'{caminho}arquivo_teste_1_12.txt', 'a') as f:
    f.writelines(s)

# ########################################
texto_2 = texto + '\n'
s2 = [f'{linha}\n' for linha in s]
with open(f'{caminho}arquivo_teste_2_12.txt', 'w') as f:
    f.write(texto_2)
    f.writelines(s2)

# ########################################
with open(f'{caminho}arquivo_teste_3_12.txt', 'w') as f:
    print(texto, file=f)
    for linha in s:
        print(linha, file=f)
