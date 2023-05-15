class Solution:
    def minimumEffortPath(self, heights: List[List[int]]) -> int:
        linhas, colunas = len(heights), len(heights[0])
        
        # Armazenando todas as direções possíveis (cima, baixo, direita e esquerda)
        possiveisDirecoes = [(1, 0), (-1, 0), (0, 1), (0, -1)] 
        
        # Inicializando a matriz de distâncias com valor infinito, exceto a posição inicial (0, 0) que recebe 0
        distancia = [[float('inf')] * colunas for _ in range(linhas)]
        distancia[0][0] = 0
        
        # Fila de prioridade para armazenar os nós visitados, com cada elemento da fila contendo distância atual, linha e coluna do nó
        filaDePrioridade = [(0, 0, 0)]
        
        while (filaDePrioridade):
            # Obtém o nó com menor distância atual
            esforco, linha, coluna = heapq.heappop(filaDePrioridade)
            
            # Verifica se já chegou no vértice final (linha, coluna)
            if ((linha == linhas-1) and (coluna == colunas-1)):
                return esforco
            
            # Verifica se o esforço é maior do que o armazenado até agora
            if (esforco > distancia[linha][coluna]):
                continue
            
            for deslocamentoLinha, deslocamentoColuna in possiveisDirecoes:
                novaLinha, novaColuna = linha + deslocamentoLinha, coluna + deslocamentoColuna
                
                # Verifica se o novo nó está dentro dos limites da matriz
                if ((0 <= novaLinha < linhas) and (0 <= novaColuna < colunas)):
                
                # Calcula o esforço necessário para ir do nó atual para o novo nó
                    diferenca = heights[linha][coluna] - heights[novaLinha][novaColuna]
                    if (diferenca < 0):
                        diferenca = diferenca * (-1)
                    
                    if(esforco > diferenca):
                        novoEsforco = esforco
                    else:
                        novoEsforco = diferenca

                    # Verifica se o novo esforço é menor do que o atual
                    if (novoEsforco < distancia[novaLinha][novaColuna]):
                        distancia[novaLinha][novaColuna] = novoEsforco
                        heapq.heappush(filaDePrioridade, (novoEsforco, novaLinha, novaColuna))
        
        return distancia[linhas-1][colunas-1]
