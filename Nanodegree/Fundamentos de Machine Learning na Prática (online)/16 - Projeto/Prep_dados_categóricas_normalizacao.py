from xml.dom import XML_NAMESPACE
import pandas as pd
import matplotlib.pyplot as plt
from sklearn import preprocessing

base = pd.read_csv(
    r'C:\Users\lexus\Documents\Estudos\Impacta_2023\Nanodegree\Fundamentos de Machine Learning na Prática (online)\16 - Projeto\modelagem_rh.csv')

print('==Tipos de Dados==')
print(base.info())

print('==Verifica se possui dados nulos==')
print(base.isnull().sum())

print('==Base com valores nulos para nivel_satisfação==')
print(base.nivel_satisfacao.isnull())

# inserindo dados no campos nulos
base.loc[base.nivel_satisfacao.isnull(), 'nivel_satisfacao'] = \
    base.nivel_satisfacao.mean()

print('==Base com valores nulos para nivel_satisfação==')
print(base.isnull().sum())


# transformar dados categoricos em binarios
base = pd.get_dummies(base, drop_first=True)

# alterar tipo de dados para inteiro
base.departamento_RandD = base.departamento_RandD.astype(int)
base.departamento_accounting = base.departamento_accounting.astype(int)
base.departamento_hr = base.departamento_hr.astype(int)
base.departamento_management = base.departamento_management.astype(int)
base.departamento_marketing = base.departamento_marketing.astype(int)
base.departamento_product_mng = base.departamento_product_mng.astype(int)
base.departamento_sales = base.departamento_sales.astype(int)
base.departamento_support = base.departamento_support.astype(int)
base.departamento_technical = base.departamento_technical.astype(int)
base.salario_low = base.salario_low.astype(int)
base.salario_medium = base.salario_medium.astype(int)

print('==Tipos de Dados==')
print(base.info())
print('==Verifica se possui dados nulos==')
print(base.isnull().sum())

print('==Escala de valores dos atributos==')
print(base.max())

print('==Valores Maximo e Minimos==')
max_min = pd.DataFrame([base.max(), base.min()], index=['Max', 'Min']).T
print(max_min)

x = base.values
minmax = preprocessing.MinMaxScaler()
x_scaled = minmax.fit_transform(x)

base = pd.DataFrame(x_scaled, columns=base.columns)
print(base.head)

print('==Valores Maximo e Minimos==')
max_min = pd.DataFrame([base.max(), base.min()], index=['Max', 'Min']).T
print(max_min)
