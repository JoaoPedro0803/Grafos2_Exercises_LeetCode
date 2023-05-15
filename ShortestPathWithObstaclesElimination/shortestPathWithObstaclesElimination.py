class Solution:
    def shortestPath(self, grid: List[List[int]], k: int) -> int:
        numLinhas, numColunas = len(grid), len(grid[0])
        
        # Armazenando todas as direções possíveis (cima, baixo, direita e esquerda)
        possiveisDirecoes = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        
        # Inicializando a matriz de distâncias com infinito, exceto para o nó inicial
        distancias = [[float('inf')] * numColunas for _ in range(numLinhas)]
        distancias[0][0] = 0
        
        # Criando uma fila de prioridade vazia para armazenar os nós a serem visitados, tendo respectivamente distância, linha, coluna, obstáculos restantes 
        filaDePrioridade = [(0, 0, 0, k)]
        
        # Executando o algoritmo de Dijkstra
        while (filaDePrioridade):
            distancia, linha, coluna, obstaculos = heapq.heappop(filaDePrioridade)
            
            # Verificando se chegou ao nó de destino
            if ((linha == numLinhas - 1) and (coluna == numColunas - 1)):
                return distancia
            
            # Verificando se já foi visitado com número menor ou igual de obstáculos
            if ((distancia > distancias[linha][coluna]) or (obstaculos < 0)):
                continue
            
            # Explorando os vizinhos do nó atual
            for deslocamentoLinha, deslocamentoColuna in possiveisDirecoes:                
                novaLinha = linha + deslocamentoLinha
                novaColuna = coluna + deslocamentoColuna

                # Verificando se o nó vizinho está dentro dos limites da matriz
                if ((0 <= novaLinha < numLinhas) and (0 <= novaColuna < numColunas)):
                    novosObstaculos = obstaculos - grid[novaLinha][novaColuna]
                    novaDistancia = distancia + 1
                    
                    # Verificando se o caminho atual é mais curto do que o caminho registrado na matriz de distâncias
                    if (novaDistancia < distancias[novaLinha][novaColuna]):
                        distancias[novaLinha][novaColuna] = novaDistancia
                        heapq.heappush(filaDePrioridade, (novaDistancia, novaLinha, novaColuna, novosObstaculos))
        
        # Se não for possível encontrar um caminho válido, retorna -1
        return -1