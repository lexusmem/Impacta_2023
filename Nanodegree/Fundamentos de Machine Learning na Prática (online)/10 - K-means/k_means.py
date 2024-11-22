import pandas as pd
from sklearn.cluster import KMeans, k_means
import pprint
import numpy as np
import matplotlib.pyplot as plt
# aprendizagem não supervisionada
# distancia padrão euclidiana

base = pd.read_csv(
    r'C:\Users\lexus\Documents\Estudos\Impacta_2023\Nanodegree\Fundamentos de Machine Learning na Prática (online)\10 - K-means\compras_supermercado.csv')

print('==Linhas e Colunas==')
linhas_colunas = base.shape
print(type(linhas_colunas))
print(linhas_colunas)

print('==Primeiros Itens da Base==')
print(base.head())

# calculo de centroides para encontrar os grupos
# 4 grupos
# 1000 recalculos
kmeans = KMeans(n_clusters=4, max_iter=1000)

kmeans.fit(base)

print('==Distribuição de grupos para cada objeto==')
lista_labels = kmeans.labels_
print(lista_labels)

print('==Centroide de cada grupo - valor medio de cada grupo==')
centroides = kmeans.cluster_centers_
for n in range(len(centroides)):
    pprint.pprint(centroides[n])

print('==Valores calculados para cada grupo==')
print(pd.DataFrame(kmeans.cluster_centers_, columns=base.columns))

print('==Qtd de objetos para cada um dos grupos==')
grupo, frequencia = np.unique(lista_labels, return_counts=True)
print(grupo)
print(frequencia)

print('==distribuição dos dados de forma grafica - Grupo 1==')
base[kmeans.labels_ == 0].hist()
plt.show()

print('==distribuição dos dados de forma grafica - Grupo 2==')
base[kmeans.labels_ == 1].hist()
plt.show()

print('==distribuição dos dados de forma grafica - Grupo 3==')
base[kmeans.labels_ == 2].hist()
plt.show()

print('==distribuição dos dados de forma grafica - Grupo 4==')
base[kmeans.labels_ == 3].hist()
plt.show()
