import this

caminho = '.\\Impacta_2023\\Analise e Desenvolvimento de Sistema\\2_Semestre\\Programação_Orientada_a_Objetos\\'

arquivo = open(f"{caminho}zenofpython_12.txt", "r")
print('\n')
print(arquivo)

# verificar se o arquivo está fechado.
print(arquivo.closed)

# para ler o arquivo
# ler todas as linhas
conteudo_arquivo = arquivo.read()
print(conteudo_arquivo)
print(type(conteudo_arquivo))

# ler linha
# linha = arquivo.readline()
# ler linhas
# linhas = arquivo.readlines()
arquivo.close()
print(arquivo.closed)

# criar arquivo e escrever
# abrir arquivo no modo escrita para alteração
# Se não existir o arquivo automaticamente é gerado um novo.
novo_arquivo = open(f"{caminho}teste_12.txt", "w")
# Tenha cuidado ao usar o modo w, pois ele sobrescreve o conteúdo existente do
# arquivo.

# Escrever no arquivo criado
novo_arquivo.write('Teste de escrita.\n')
# Utilize flush() para garantir que as alterações sejam escritas no disco
# antes de fechar o arquivo.
novo_arquivo.flush()


# Abrir no modo leitura
novo_arquivo = open(f"{caminho}teste_12.txt", "r")

# ler o arquivo
conteudo_novo_arquivo = novo_arquivo.read()

# imprimir arquivo
print(conteudo_novo_arquivo)

# abrir arquivo no modo 'a' append para incluir nova escrita.
novo_arquivo = open(f"{caminho}teste_12.txt", "a")
# função write para escrita.
novo_arquivo.write('Teste de escrita na segunda linha.\n')
# Utilize flush() para garantir que as alterações sejam escritas no disco
# antes de fechar o arquivo.
novo_arquivo.flush()
# abrir arquivo modo 'r' read
novo_arquivo = open(f"{caminho}teste_12.txt", "r")
print(novo_arquivo.read())

# abrir arquivo no modo append para incluir nova escrita.
with open(f"{caminho}teste_12.txt", "a") as f:
    f.write('Teste de escrita na terceira linha.\n')
    # Utilize flush() para garantir que as alterações sejam escritas no disco
    # antes de fechar o arquivo.
    f.flush()

# abrir arquivo modo 'r' read
novo_arquivo = open(f"{caminho}teste_12.txt", "r")
print(novo_arquivo.read())

# novo_arquivo.close()
print(f'Arquivo fechado: {novo_arquivo.closed}.')
print(novo_arquivo)

# Se precisar configurar o enconding por causa do acento utilizar cp1252
# ou utf-8
with open(f"{caminho}teste_2_12.txt", "w", encoding='cp1252') as f:
    f.write('Olá!')

with open(f"{caminho}teste_2_12.txt", "r") as f:
    print(f.read())
    print(f.closed)

print('\n')
print(f)
print(f.closed)
