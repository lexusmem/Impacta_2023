import pandas as pd
from sklearn.tree import DecisionTreeClassifier
from sklearn.tree import export_graphviz

base = pd.read_excel(
    r'C:\Users\lexus\Documents\Estudos_Programação\Impacta_2023\Nanodegree\Fundamentos de Machine Learning na Prática (online)\4 - KNN\funcionarios.xlsx')

# listando os 5 primeiros registros
# print(base.head())

# listando os 7 primeiros registros
# print(base.head(7))

# excluindo uma coluna
del base['Unnamed: 0']

# listando os 5 primeiros registros
# print(base.head())

# todas as linhas, menos a última coluna
X = base.iloc[:, :-1]
# print(X)

# impressão das colunas
print('===COLUNAS===')
print(X.columns)

# todas as linhas, somente a última coluna
y = base.iloc[:, -1]
# print(y)

# visualizar linguagem únicas da base
print('===LINGUAGENS ÚNICAS===')
linguagens = base.linguagem.unique()
print(linguagens)

# hiper parametros utilizados foi o padrão
tree = DecisionTreeClassifier()

# treinamento para tomada de decisão com base na nossa amostra
tree.fit(X, y)

# selecionando uma linha qualquer sem a ultima coluna que seria
# a linguagem da pessoa
amostra = base.sample()

# printando amostra selecionada para  utilização na arvore
print('===AMOSTRA SELECIONADA===')
print(amostra)

# passando a amostra na arvore para demonstrar o resultado
resultado = tree.predict(amostra.iloc[:, :-1])

# imprimindo o resultado do treinamento e se o treinamento for correto o ideal
# é que apresente a mesma linguagem da amostra
print('===RESULTADO AMOSTRA SELECIONADA===')
print(resultado)

# é possível inserir os dados manualmente nos modelo para treinamento
teste_manual = tree.predict([[2, 0, 0, 1, 1, 0]])
print('===RESULTADO TESTE MANUAL===')
print(teste_manual)

# visualizar arvore de decisão
arquivo = open('arvore.dot', 'w')
# criando o gráfico para visualização
export_graphviz(tree, out_file=arquivo,
                feature_names=X.columns, class_names=linguagens)
# fechando o arquivo
arquivo.close()
