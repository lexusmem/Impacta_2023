import meu_modulo_09
import sys

# utilizando uma função do modulo importado meu_modulo_09
meu_modulo_09.exibe_nome()

# utilizando uma classe do modulo importado meu_modulo_09
alex = meu_modulo_09.Teste()

# criando uma variável teste.
variavel = 'teste'

# A função dir() em Python é uma função embutida que retorna uma lista de
# nomes (strings) que representam os atributos e métodos de um objeto. Essa
# lista inclui tanto os atributos e métodos públicos quanto os privados, mesmo
# os built-in que são padrão para todos os objetos.

# retornando os atributos e métodos deste arquivo.
print('\n')
print(dir())

# retornando os atributos e métodos deste arquivo.
print('\n')
print(dir(meu_modulo_09))
print(type(meu_modulo_09.variavel))
print(meu_modulo_09.variavel)

# sys é o modulo que trabalha com o sistema operacional.
# sys.path em Python é uma lista que define o caminho de pesquisa de módulos
# do interpretador Python. Ele determina os diretórios onde o interpretador
# irá procurar módulos importados usando a instrução import.
print('\n')
print(sys.path)

# é possível inserir novo caminho no path para procurar módulos novo caminho
sys.path.insert(0, 'novo\caminho')
print('\n')
print(sys.path)

# sys.executable indica onde está sendo executado o python
print('\n')
print(sys.executable)
