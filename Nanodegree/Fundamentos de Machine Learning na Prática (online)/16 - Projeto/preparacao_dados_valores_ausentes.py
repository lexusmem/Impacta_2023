import pandas as pd
import matplotlib.pyplot as plt

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
