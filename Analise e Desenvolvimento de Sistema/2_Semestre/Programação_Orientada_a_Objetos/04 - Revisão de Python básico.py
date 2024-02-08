# Input solicita que o usuário digite um valor.
# Sempre retorno valor do tipo int
# num = input('Digite um número: ')
# print(f'{num} é do tipo {type(num)}')

# tipos de objetos

# int = 1, -5, 80

# float = 3.0, -1.2, 5., .7

# str = 'ola', "ola", '''ola''', """ola"""

# classe define o tipo do objeto.

print(type(.7))

tipo_string = 'olá'

print(type(tipo_string))

TIPO_BOOL = True

print(type(TIPO_BOOL))

print('''ola
      como está as coisas
      teste de pular linhas''')
print("""teste
pular linha \n
      para ver se funciona""")

# Variáveis
'''
Uma variável em Python é um espaço na memória do computador que armazena um
valor. É como se fosse um caixa com um nome, onde você guarda informações
para usá-las posteriormente no seu programa.

Características das variáveis em Python:

Nome: É o identificador da variável, que você escolhe e deve seguir algumas
regras:
Começar com letra minúscula ou "_".
Conter apenas letras, números e "_".
Não ser uma palavra-chave reservada da linguagem.
Valor: É o conteúdo armazenado na variável, que pode ser de diferentes tipos,
como:
Inteiros (int): Números sem casas decimais (ex: 1, 2, 3).
Ponto flutuante (float): Números com casas decimais (ex: 1.5, 2.75).
Texto (str): Sequências de caracteres (ex: "Olá, mundo!", "Python").
Booleano (bool): Valores True ou False.
Listas: Coleções ordenadas de valores.
Dicionários: Coleções de pares chave-valor.
Tipo: É a categoria do valor armazenado na variável, que define as operações
que podem ser realizadas com ela. O tipo de variável em Python é dinâmico,
o que significa que você não precisa declará-lo explicitamente.
'''

exemplo_de_variavel = "teste de variável"
print(exemplo_de_variavel)

help('keywords')

# Operadores
'''
Operadores Aritméticos
Operadores de Atribuição
Operadores de Comparação
Operadores Lógicos
Operadores de Identidade
'''

print(29/5)

# divisão inteira
print(29//5)

# Resto da divisão
print(29 % 5)

# Operadores unarios (- e +)
# -5, +6

# Funções
# Funções são blocos de código reutilizáveis que realizam uma
# tarefa específica. Elas ajudam a organizar o código, tornando-o
# mais legível e modular.


def saudacao(nome):
    """
    Esta função recebe uma string (nome) como parâmetro e imprime uma saudação.
    """
    print(f"Olá, {nome}!")


saudacao('alex')


def soma(a, b):
    """
    Esta função retorna a soma de dois números.
    """
    resultado = a + b
    return resultado


somar = soma(10, 20)
print(somar)

# Funções anônimas (lambda):
'''
São funções pequenas e anônimas definidas usando a palavra-chave lambda.
Elas podem ter qualquer número de argumentos, mas apenas uma expressão como
corpo da função. Por exemplo:
'''
def quadrado(x): return x * 2


print(quadrado(1))
print(quadrado("a"))

# funções integradas (built-in functions)

print(round(100.68665, 2))
'''
Funções de Conversão de Tipo:

int(): Converte um valor para inteiro.
float(): Converte um valor para ponto flutuante.
str(): Converte um valor para string.
bool(): Converte um valor para booleano.

Funções de Sequência:

len(): Retorna o comprimento de uma sequência (lista, tupla, string, etc.).
max(): Retorna o valor máximo em uma sequência.
min(): Retorna o valor mínimo em uma sequência.
sum(): Retorna a soma dos elementos em uma sequência numérica.

Funções de Iteração e Controle de Fluxo:

range(): Retorna uma sequência imutável de números.
enumerate(): Retorna um objeto enumerado.
zip(): Combina múltiplas sequências em uma única sequência de tuplas.
sorted(): Retorna uma nova lista ordenada a partir dos elementos de uma
sequência.

Funções de Entrada e Saída:

print(): Imprime valores na saída padrão.
input(): Lê uma entrada do usuário.

Funções de Gerenciamento de Arquivos:

open(): Abre um arquivo.
close(): Fecha um arquivo.
read(): Lê o conteúdo de um arquivo.
write(): Escreve dados em um arquivo.

Funções Matemáticas:

abs(): Retorna o valor absoluto de um número.
pow(): Retorna a potência de um número.
round(): Arredonda um número para um número específico de casas decimais.
Funções de Strings:

capitalize(): Converte o primeiro caractere de uma string para maiúsculo.
lower(): Converte uma string para minúsculas.
upper(): Converte uma string para maiúsculas.
split(): Divide uma string em substrings com base em um delimitador.
Funções de Controle de Fluxo:

if, elif, else: Estruturas condicionais.
for: Loop de iteração.
while: Loop de repetição.
'''

print(dir(__builtins__))
