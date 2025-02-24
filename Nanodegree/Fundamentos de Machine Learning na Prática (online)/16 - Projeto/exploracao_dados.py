import pandas as pd
import matplotlib.pyplot as plt

base = pd.read_csv(
    r'C:\Users\lexus\Documents\Estudos\Impacta_2023\Nanodegree\Fundamentos de Machine Learning na Prática (online)\16 - Projeto\modelagem_rh.csv')

print('==Linhas e Colunas==')
linhas_colunas = base.shape
print(linhas_colunas)

print('==Primeiros Registros da Base==')
print(base.head())

print('==Qtd que saiu da Empresa==')
print(base.saiu.value_counts())

print('==Percentual que saiu da Empresa==')
print(base.saiu.value_counts()/len(base)*100)

print('==Grafico==')
base.saiu.value_counts().plot(kind='bar')
# plt.show()
base.saiu.value_counts().plot(kind='bar')
# plt.xticks((0, 1), ['Saiu', 'Não Saiu'])
# plt.show()

print('==Verificar de qual departamento saiu mais Pessoas==')
departamento_saiu = pd.crosstab(base.departamento, base.saiu)
print('==Qtd saida ou não por departamento==')
print(departamento_saiu)
valores = departamento_saiu.sum(axis=1)
print('==Total por departamento==')
print(valores)
percentual_de_saida_departamento = departamento_saiu.divide(
    valores, axis=0)*100
print('==Percentual de saida/permanencia por departamento==')
print(percentual_de_saida_departamento)

print('==Verificar qual salario saiu mais Pessoas==')
salario_base_saiu = pd.crosstab(base.salario, base.saiu)
print(salario_base_saiu)
valores_salario = pd.crosstab(base.salario, base.saiu)
soma_salario = valores_salario.sum(axis=1)
percentual_saida_salario = valores_salario.divide(soma_salario, axis=0)*100

print('==Percentual de saida por salario==')
print(percentual_saida_salario)
percentual_saida_salario.plot(kind='bar', stacked=True)
plt.show()
