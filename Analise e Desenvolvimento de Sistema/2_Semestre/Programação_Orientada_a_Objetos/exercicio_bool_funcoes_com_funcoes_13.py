"""
Com base no exemplo acima, crie uma função de filtro, que irá receber dois
parâmetros: uma função f e uma sequência s, e deve retornar uma lista contendo
apenas os itens da sequência para os quais a função f retornar True. A função
f deve receber um parâmetro e retornar um verdadeiro ou falso, baseado no
parâmetro recebido.
"""


def converte(f, s):
    nova_lista = []
    for x in s:
        if f(x) == True:
            nova_lista.append(f'{x} -> {f(x)}')
    return nova_lista


alex = [0, 1, 10 > 1, 10 < 1]

print(converte(bool, alex))

teste_map = map(bool, alex)
print(list(teste_map))
