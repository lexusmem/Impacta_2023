import os
import re

diretorio = r'C:\Users\lexus\Documents\Estudos\Impacta_2023\Analise e Desenvolvimento de Sistema\3_Semestre\Desenvolvimento_com_Automação_Robótica_de_Processos_RPA\regex'

# indicacoes = ''
for arqEmail in os.listdir(diretorio):
    if arqEmail.endswith('.html'):
        arquivo = open(diretorio + "\\" + arqEmail, 'r', encoding='utf-8')
        texto_arquivo = arquivo.read()
        # elimina final do email depois de alex sousa
        texto_limpo = re.sub(r'(Alex Sousa(.|\s)*)', "", texto_arquivo)
        # Elimina os "pula de linhas" e "*" por "".
        texto_limpo = re.sub(r'(\n|\*)', "", texto_limpo)
        # Remover múltiplos espaços.
        texto_limpo = re.sub(r'\s+', " ", texto_limpo)
        print(texto_limpo)
        aux1 = re.findall(r"(Título:\s*(.+?)\s*-\sAutor)", texto_limpo)
        print(aux1[0][0])
        aux2 = re.findall(r"(Autor Principal:\s*(.+?)\s*-\sAno)", texto_limpo)
        print(aux2[0][0])
        aux3 = re.findall(r"(Ano de Publicação:\s*(\d{4}))", texto_limpo)
        print(aux3[0][0])
        print('='*10)


# texto = "Eba deu Certo Alex Sousa: Teste de exclusão de texto"
# texto_limpo = re.sub(r'(Alex Sousa(.|\s)*)', "", texto)
# print(texto_limpo)
