import pandas as pd
from sklearn.neighbors import KNeighborsClassifier


print(f'Versão dos pandas {pd.__version__}.')

base = pd.read_excel(
    r'C:\Users\lexus\Documents\Estudos\Impacta_2023\Nanodegree\Fundamentos de Machine Learning na Prática (online)\4 - KNN\funcionarios.xlsx')

# saber qtd de linhas e colnas
print('(LINHAS, COLUNAS)')
print(base.shape)

# dados das colunas e dados das 5 primeiras linhas
print(base.head())

print('===TESTE 1===')
# retorna o nome da coluna e os dados da primeira linha
print(base.loc[0])

# .columns nome das colunas
dados_colunas = list(base.columns)

print('===IMPRESSÃO DOS NOMES DAS COLUNAS===')
# iterando sobre os dados da coluna
for x in range(len(dados_colunas)):
    print(dados_colunas[x])
print(f'Total de colunas {x+1}.')

# exclusão de colunas
del base['Unnamed: 0']

# apresentando dados da base sem a coluna excluída acima
print(base.head(10))

# X entrada de modelo
# iloc informa um DataFrame linhas e colunas a serrem utilizadas
# todas as linas, :-2 até a penúltima coluna
X = base.iloc[:, :-1]

print(X)

# Y saidas de modelo
# iloc informa um DataFrame linhas e colunas a serrem utilizadas
# todas as linas :, -1 e a última coluna coluna

Y = base.iloc[:, -1]

print(Y)

knn = KNeighborsClassifier(n_neighbors=3)

# função fit responsável por fazer o treinamento
# nesta fun usamos como hyperparameter o numero de vizinhos 3 para resultado
resultado = knn.fit(X, Y)
print(resultado)

# pegamos uma das linha aleatoria para usar na função fit
amostra = base.sample()
print(amostra)

# retiramos esta linha do total para não da erro
amostra.iloc[:, :-1]
teste = knn.predict(amostra.iloc[:, :-1])
print('===Resutado com base dos dados da amostra===')
print(teste)
