def emite_senha(nome, senha):
    return f'Olá {nome}, sua senha é {senha}.'


d = {'nome': 'Alex', 'senha': '1'}


"""
O asterisco duplo faz o desempacotamento de dicionários para funções, passando
seu conteúdo como argumentos nomeados para a função, sendo a chave do
dicionário o nome do parâmetro e o valor do dicionário o valor passado como
argumento para aquele parâmetro
"""
print(emite_senha(**d))
