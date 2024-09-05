# K-Means Clustering Algorithm

Este repositório contém uma implementação do algoritmo de agrupamento K-Means. A função principal organiza amostras de dados em K grupos (clusters), ajustando os centroides de cada cluster a cada iteração até que os resultados se estabilizem ou o número máximo de iterações seja atingido.

## Funcionalidades

- **K-Means Clustering**: Agrupa os dados em K clusters com base nas coordenadas fornecidas.
- **Cálculo de Distância Euclidiana**: Utiliza a fórmula da distância euclidiana para medir a proximidade entre pontos.
- **Atualização de Centroides**: Recalcula os centroides de cada cluster após a realocação dos pontos.
- **Número Variável de Iterações**: O algoritmo pode rodar por um número máximo de iterações definido pelo usuário.
- **Saída em Arquivo**: Gera um arquivo com os clusters finais e as amostras associadas a cada um.

## Requisitos

- **Python 3.x**
- Bibliotecas:
  - `pandas`
  - `numpy`
  - `math`

## Instalação

1. Clone o repositório:
   ```bash
   git clone https://github.com/seu-usuario/kmeans-algorithm.git

2. Instale as depêndencias:
   ```bash
   pip install pandas numpy
   ```
## Como usar

1. Substitua o caminho do arquivo de dados no código
   ```bash
   caminho_arquivo = '/caminho/para/seu/arquivo.txt'
   ```
2. Execute o script e forneça os parâmetros quando necessário
     * Número de clusters (K).
     * Número máximo de iterações.
       
3. A saída final será gravada em um arquivo chamado resultado_particao.txt no mesmo diretório.

## Arquivo de dados

O arquivo deve conter amostras organizadas no seguinte formato:
```bash
sample_label   d1   d2
ponto1         1.0  2.0
ponto2         3.0  4.0
...
```
Onde:
  * `sample_lable`: Identificador da amostra(ponto).
  * `d1` e `d2`: Corrdenadas da amostra.

Certifique-se de que o arquivo seja lido corretamente no formato .txt com tab como delimitador.



  



