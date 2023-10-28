# 1) Crie um programa que solicite ao usuário um número de 1 à 7 e
# exiba o dia da semana correspondente. Assuma que a semana começa
# no domingo (1) e termina no sábado (7). Use apenas seleção simples,
# ou seja, sem else nem elif.

dia_semana = int(input('Digite um número de 1 a 7 para o dia da semana: '))

if dia_semana == 1:
    print('Domingo')
if dia_semana == 2:
    print('Segunda')
if dia_semana == 3:
    print('Terça')
if dia_semana == 4:
    print('Quarta')
if dia_semana == 5:
    print('Quinta')
if dia_semana == 6:
    print('Sexta')
if dia_semana == 7:
    print('Sábado')

# 2) Refaça o exercício anterior, agora utilizando a seleção encadeada,
# mas sem usar o comando elif, de modo que seja observada a importância
#  do alinhamento correto de indentação entre os diversos comandos if e else.

dia_semana = int(input('Digite um número de 1 a 7 para o dia da semana: '))

if dia_semana == 1:
    print('Domingo')
else:
    if dia_semana == 2:
        print('Segunda')
    else:
        if dia_semana == 3:
            print('Terça')
        else:
            if dia_semana == 4:
                print('Quarta')
            else:
                if dia_semana == 5:
                    print('Quinta')
                else:
                    if dia_semana == 6:
                        print('Sexta')
                    else:
                        if dia_semana == 7:
                            print('Sábado')

# 3) Refaça o exercício anterior, agora utilizando elif.

dia_semana = int(input('Digite um número de 1 a 7 para o dia da semana: '))

if dia_semana == 1:
    print('Domingo')
elif dia_semana == 2:
    print('Segunda')
elif dia_semana == 3:
    print('Terça')
elif dia_semana == 4:
    print('Quarta')
elif dia_semana == 5:
    print('Quinta')
elif dia_semana == 6:
    print('Sexta')
elif dia_semana == 7:
    print('Sábado')
