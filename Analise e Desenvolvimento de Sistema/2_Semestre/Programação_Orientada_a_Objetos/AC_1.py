valores = [1, 2, 3, 4]
novo = []

for n in valores:
    novo.append(n**2)

print(novo)


def eh_palindromo(texto):
    for i in range(len(texto)):
        if texto[i] != texto[-1-i]:
            return False
    return True


entradas = ['arara', 'elefante', 'radar', 'banana']
palindro = []

for palavra in entradas:
    if (eh_palindromo(palavra)):
        palindro.append(palavra)

print(palindro)
