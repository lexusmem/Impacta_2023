# se n=4 o programa deverá exibir 0 1 2 3 e, na próxima linha, 3 2 1 0
n = int(input('n? '))
comeco = 0
final = n
passo = -1

for i in range(comeco, final):
    print(i, end=' ')
print()
for i in range(final - 1, comeco - 1, passo):
    print(i, end=' ')

print()

frase = 'teste de inteligencia do cigapura pode ser executa!'
tamanho = len(frase)
print(frase[tamanho - 1])
print(frase)
