
import pandas as pd
import numpy as np
import math


def distancia_euclidiana(x1, x2, y1, y2):
    return np.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)

def calcular_distancia_entre_nomes(df, nome_ponto1, nome_ponto2):
    # Obtém as coordenadas dos pontos
  ponto1 = df[df['sample_label'] == nome_ponto1]
  ponto2 = df[df['sample_label'] == nome_ponto2]

    # Extrai as coordenadas
  x1, y1 = ponto1[['d1', 'd2']].values[0]
  x2, y2 = ponto2[['d1', 'd2']].values[0]

    # Calcula a distância euclidiana
  distancia = distancia_euclidiana(x1, x2, y1, y2)

  return distancia

def extrair_numero(nome):
    # Encontrar o último prefixo 's' para extrair o número
    partes = nome.split('s')
    if len(partes) > 1:
        return int(partes[-1])  # O último elemento após 's' é o número
    return float('inf')  # Caso padrão, para valores não válidos

def extrair_numero(nome):
    partes = nome.split('s')
    if len(partes) > 1:
        return int(partes[-1])  # O último elemento após 's' é o número
    return float('inf')  # Caso padrão, para valores não válidos

def ordenar_clusters(cluster):

  cluster_ordenado = sorted(cluster, key=extrair_numero)

  return cluster_ordenado


def calcular_distancia_entre_pontos(df, nome_ponto1, centroide):
    # Obtém as coordenadas dos pontos
  ponto1 = df[df['sample_label'] == nome_ponto1]

    # Extrai as coordenadas
  x1, y1 = ponto1[['d1', 'd2']].values[0]

    # Calcula a distância euclidiana
  distancia = distancia_euclidiana(x1, centroide[0], y1, centroide[1])

  return distancia

def calcular_centroide(arquivo, cluster, k):
  # Filtra o DataFrame para obter apenas as amostras que pertencem ao cluster
  cluster_df = arquivo[arquivo['sample_label'].isin(cluster)]

    # Calcula a média das coordenadas d1 e d2 para o cluster
  centroide_d1 = cluster_df['d1'].mean()
  centroide_d2 = cluster_df['d2'].mean()

    # Retorna o centroide
  return (centroide_d1, centroide_d2)

# Substitua 'caminho_para_o_arquivo.txt' pelo caminho real do seu arquivo
caminho_arquivo = '/content/DadosKatti/datasets/c2ds3-2g.txt'

# Lê o arquivo .txt e cria o DataFrame
df = pd.read_csv(caminho_arquivo, delimiter='\t')

# Exibe o DataFrame
print(df)


valor_k = int(input("Digite o número de clusters desejados: "))
max_itera = int(input("Insira o número máximo de iterações a serem realizadas: "))


def criar_cluster(arquivo, k):
  clusters = []
  for cluster in range(k):
    lista = []
    clusters.append([])
  contador_aux = 0
  for valor in arquivo.sample_label:
    clusters[int(contador_aux/(len(arquivo)/k))].append(valor)
    contador_aux+=1
  return clusters

def atribui_centroides(clusters, k):
  centroides = []
  for i in range(k):
    centroides.append(clusters[i][0])
  return centroides

def atualiza_cluster(dist, k):
  clusters = []
  for cluster in range(k):
    lista = []
    clusters.append([])
  for i in (dist):
    menor = min(i[1:])
    indice_minimo = i.index(menor)
    clusters[indice_minimo-1].append(i[0])

  return clusters

def atualiza_centroides(arquivo, clusters, k):
  centroides = []
  for i in range(k):
    centroides.append(calcular_centroide(arquivo, clusters[i], k))
  return centroides

def kmedias(arquivo, k, max_itera):
  clusters = criar_cluster(arquivo, k)
  centroides = atribui_centroides(clusters, k)


  #PRIMEIRA ITERAÇÃO

  print("======================\nPRIMEIRA ITERAÇÃO\n======================\n")
  print("PRIMEIROS CLUSTERS E CENTROIDES")
  for i in clusters:
    print(i, "\n")
  print("CENTROIODES: ", centroides, "\n")

  dist = []
  for i in range(k):
    for j in range(len(clusters[i])):
      lista_dist = []
      lista_dist.append(clusters[i][j])
      for w in range(k):
        lista_dist.append(calcular_distancia_entre_nomes(arquivo, clusters[i][j], centroides[w]))
      dist.append(lista_dist)
  for i in dist:
    print(i)

  clusters = atualiza_cluster(dist, k)

  print('\n\n\n')
  print("CLUSTERS ATUALIZADOS: ")
  for i in clusters:
    print(i, "\n")

  novos_centroides = atualiza_centroides(arquivo, clusters, k)
  print("\n\nNOVOS CENTROIDES: ", novos_centroides)

  if novos_centroides == centroides:
    print("\n===============\nPAREI PORQUE NÃO MUDARAM OS CENTROIDES\n===============\n")
    return

  else:
    centroides = novos_centroides

  #MAIS ITERAÇÕES
  for it in range(max_itera-1):
    dist = []
    for i in range(k):
      for j in range(len(clusters[i])):
        lista_dist = []
        lista_dist.append(clusters[i][j])
        for w in range(k):
          lista_dist.append(calcular_distancia_entre_pontos(arquivo, clusters[i][j], centroides[w]))
        dist.append(lista_dist)
    for i in dist:
      print(i)

    clusters = atualiza_cluster(dist, k)

    print('\n\n\n')
    print("CLUSTERS ATUALIZADOS: ")
    for i in clusters:
      print(i, "\n")

    novos_centroides = atualiza_centroides(arquivo, clusters, k)
    print("\n\nNOVOS CENTROIDES: ", novos_centroides)

    if novos_centroides == centroides:
      print("\n===============\nPAREI PORQUE NÃO MUDARAM OS CENTROIDES\n===============\n")

      with open('resultado_particao.txt', 'w') as f:

        for i in range(k):
          clusters[i] = ordenar_clusters(clusters[i])
          print(clusters[i])


        for i in  range(k):
          for j in range(len(clusters[i])):
              nome_objeto = clusters[i][j]
              cluster = i
              f.write(f"{nome_objeto}\t{cluster}\n")

      return

    else:
      centroides = novos_centroides

    if it == max_itera - 2:

      for i in range(k):
          clusters[i] = ordenar_clusters(clusters[i])

      for i in  k:
          for j in range(len(clusters[i])):
              nome_objeto = clusters[i][j]
              cluster = i
              f.write(f"{nome_objeto}\t{cluster}\n")


kmedias(df, valor_k, max_itera)
