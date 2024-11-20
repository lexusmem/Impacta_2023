from statistics import linear_regression
import pandas as pd
import matplotlib.pyplot as plt
from regex import P
from sklearn.linear_model import LinearRegression

base = pd.read_excel(
    r'C:\Users\lexus\Documents\Estudos\Impacta_2023\Nanodegree\Fundamentos de Machine Learning na Prática (online)\6 - Regressão Linear\casas.xlsx')

print('==Número de linhas e Colunas==')
n_linhas_colunas = base.shape
print(n_linhas_colunas)

print('==5 primeiros dados da base==')
# 5 primeiros dados
print(base.head())

# removendo coluna
del base['Unnamed: 0']

print('==5 primeiros dados da base==')
# 5 primeiros dados
print(base.head())

# plotar um grafico de dispersão
base.plot(kind='scatter', x='metros quadrados', y='preco')
# plt.show()

# colchetes duplos pois quero que forme um data frame
# separacao das bases
x = base[['metros quadrados']]
y = base[['preco']]

print('==Coluna Metros Quadrados==')
print(x)
print('==Coluna Metros Preco==')
print(y)

# montar regressão linear
regressao = LinearRegression()

# calcular coeficcientes da reta
regressao.fit(x, y)

# inclinação da reta calculada
print('==Inclinação da Reta==')
print(regressao.coef_)

# coeficiente linear da reta
print('==Coeficiente da Reta==')
print(regressao.intercept_)

# equação da reta
# y = coef * x + linear
equacao_reta = 280.62 * x + (-43580.74)
print('==Equação da Reta==')
print(equacao_reta)

# calcular o valor uma casa com 1500 metros quad
print('==Valor Casa==')
casa = regressao.predict([[1500]])
print(casa)

# confirmar o resultado com calculo manual
print('==Valor Casa Manual==')
casa_manual = regressao.coef_[0] * 1500 + regressao.intercept_[0]
print(casa_manual)

# calculo com mais de um atributo
# regressao linear multipla
# com varios coeficientes

base_2 = pd.read_excel(
    r'C:\Users\lexus\Documents\Estudos\Impacta_2023\Nanodegree\Fundamentos de Machine Learning na Prática (online)\6 - Regressão Linear\casas_mult.xlsx')


print('==Número de linhas e Colunas base 2==')
n_linhas_colunas = base_2.shape
print(n_linhas_colunas)

print('==5 primeiros dados da base 2==')
# 5 primeiros dados
print(base_2.head())

# removendo coluna
del base_2['Unnamed: 0']

print('==X da base 2==')
x2 = base_2[['metros quadrados', 'banheiros', 'metros sem porao', 'nota']]
print(x2.head())

print('==Y da base 2==')
y2 = base_2[['preco']]
print(y2.head())

regressa2 = LinearRegression()

regressa2.fit(x2, y2)

print('==Coeficientes Calculados da base 2==')
print(regressa2.coef_)

print('==Valor Intercept relação ao eixo y Calculados da base 2==')
print(regressa2.intercept_)

casa_multipla_valor = regressa2.predict([[1500, 1, 160, 7]])
print(casa_multipla_valor)

# equação da reta - valor esperado - exercicio
# y = coef * x + linear
exercicio_3 = 483.71 * 125 + 48864.70
print('==Equação da Reta - Resultado exercicio 3==')
print(exercicio_3)
