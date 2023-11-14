# Estruturas de repetições aninhadas

# tabuleiro
n = int(input("Informe o tamanho do tabuleiro: "))

for linha in range(n):
    for coluna in range(n):
        print("x", end=" ")
    print()

linha = 1
while linha <= n:
    coluna = 1
    while coluna <= n:
        print("x", end=" ")
        coluna += 1
    print()
    linha += 1

minuto = 60
segundo = 60

for min in range(minuto):
    for seg in range(segundo):
        print(f"{min:02}min{seg:02}s")

minutos = 0
while minutos < minuto:
    segundos = 0
    while segundos < segundo:
        print(f"{minutos:02}min{segundos:02}s")
        segundos += 1
    minutos += 1

alunos = int(input("Quantos Alunos? "))
materias = int(input("Quantas Matérias? "))


for aluno in range(alunos):
    soma = 0.0
    for materia in range(materias):
        nota = float(input(f"Informe a nota do aluno {
                     aluno+1} da materia {materia+1}: "))
        soma += nota
    soma /= materias
    print(f'A média do aluno {aluno+1} é {soma}.')
