import pandas as pd
from sklearn.tree import DecisionTreeRegressor
from sklearn.tree import export_graphviz

base = pd.read_excel(
    r'C:\Users\lexus\Documents\Estudos\Impacta_2023\Nanodegree\Fundamentos de Machine Learning na Prática (online)\7 - Árvore de Regressão\jogadores.xlsx')

print('==Linhas/Colunas==')
print(base.shape)
print('==5 Linhas da Base==')
print(base.head())

# eliminar coluna não utilizar
del base['Unnamed: 0']

X = base.iloc[:, :-1]
y = base.iloc[:, -1]

# fit faz treinamento
# predicate - faz a previsão

# importar regressor - arvore de regressao
# limitado a dois objetos para transformar uma folha
tree = DecisionTreeRegressor(min_samples_leaf=2)

# treinamento
tree.fit(X, y)

# estimar com o modelo treinado
amostra = base.sample()

print('==AMOSTRA==')
print(amostra)

print('==RESULTADO COM BASE NA AMOSTRA==')
estimacao = tree.predict(amostra.iloc[:, :-1])
print(estimacao)


# montar manual
manual = tree.predict([[1, 0, 1, 0, 1, 1]])
print('==RESULTADO COM VALORES MANUAIS==')
print(manual)

# VIZUALIZA A ávore de regressão formada
arquivo = open('arvore_regressao.dot', 'w')
export_graphviz(tree, out_file=arquivo,
                feature_names=X.columns)
arquivo.close()
