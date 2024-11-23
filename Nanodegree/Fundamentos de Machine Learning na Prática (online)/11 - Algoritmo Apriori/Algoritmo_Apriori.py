from itertools import count
import pandas as pd

base_transacinal = pd.read_csv(
    r'C:\Users\lexus\Documents\Estudos\Impacta_2023\Nanodegree\Fundamentos de Machine Learning na Prática (online)\11 - Algoritmo Apriori\lista_compras.csv')

print('==Linhas e Colunas==')
print(base_transacinal.shape)
print('==Itens bases transacional==')
print(base_transacinal.head())

# Crianção de regra apriori
# percentual de quantas vezes os itens foram comprados
sup = base_transacinal.sum()/len(base_transacinal)
# print(sup)

# itens com frequencias superios a 5%
print('==itens com frequencias superios a 5%==')
sup_itens = sup[sup >= 0.05]
print(sup_itens)


def regras_tam_2(base, itens, taxa_sup, taxa_conf):
    for i, item in enumerate(itens):
        for j in range(i+1, len(itens)):
            count_regra = len(base[(base[item] == 1) & (base[itens[j]] == 1)])
            suporte = count_regra / len(base)
            if suporte >= taxa_sup:
                count_a = len(base[base[item] == 1])
                confianca = count_regra / count_a
                if confianca >= taxa_conf:
                    print(item, '-->', itens[j], '| Suporte: ',
                          suporte, '| Confiança: ', confianca)


regras_tam_2(base_transacinal, sup_itens.index, 0.01, 0.3)


'''
Qual seria o valor do suporte das regras adiante?

Suporte (Café → Leite)
Suporte (Açúcar → Couve)
Suporte (Biscoito → Brócolis)

Considere a seguinte lista de compras:

T1 = {café, biscoito, leite}
T2 = {açúcar, banana, leite, aveia, café, couve}
T3 = {maçã, laranja, couve, açúcar}
T4 = {couve, açúcar, brócolis, café}
'''
print('==Suporte==')
print(2/4)
print(3/4)
print(0/4)

'''
Qual seria o valor da confiança para cada uma das seguintes regras?

Confiança (Café → Leite)
Confiança (Açúcar → Couve)
Confiança (Biscoito → Brócolis)

Considere a seguinte lista de compras:

T1 = {café, biscoito, leite}
T2 = {açúcar, banana, leite, aveia, café, couve}
T3 = {maçã, laranja, couve, açúcar}
T4 = {couve, açúcar, brócolis, café}
'''
print('==Confiança==')
print(2/3)
print(3/3)
print(0/1)
