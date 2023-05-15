class Solution:
    def findTheCity(self, n: int, edges: List[List[int]], distanceThreshold: int) -> int:
        # Criar o grafo usando um dicionário
        grafo = {}
        for i, j, k in edges:
            if i not in grafo:
                grafo[i] = []
            if j not in grafo:
                grafo[j] = []
            grafo[i].append((j, k))
            grafo[j].append((i, k))

        def dijkstra(noInicial):
            # Inicializar a lista de distâncias com infinito para todas as cidades, exceto a cidade inicial
            distancias = n * [float('inf')]
            distancias[noInicial] = 0

            # Fila de prioridade para armazenar os vértices visitados, onde é a distância e o vértice, respectivamente
            filaDePrioridade = [(0, noInicial)]

            while filaDePrioridade:
                # Extrair o vértice com menor distância atual
                menorDistancia, no = heapq.heappop(filaDePrioridade)

                # Verificar se já foi visitado
                if menorDistancia > distancias[no]:
                    continue

                # Atualizar as distâncias para os vizinhos do vértice atual
                if no in grafo:
                    for vizinho, pesoAresta in grafo[no]:
                        novaDistancia = menorDistancia + pesoAresta

                        # Se a nova distância for menor, ela é armazenada
                        if novaDistancia < distancias[vizinho]:
                            distancias[vizinho] = novaDistancia
                            heapq.heappush(filaDePrioridade, (novaDistancia, vizinho))

            return distancias

        # Inicializar o menor número de cidades alcançáveis com infinito e o número da cidade com maior número de cidades alcançáveis como -1
        menorNumeroCidadesAlcancaveis = float('inf')
        cidadeComMaisAlcancaveis = -1

        # Executar o algoritmo de Dijkstra para cada cidade como ponto de partida
        for i in range(n):
            distancias = dijkstra(i)
            
            # Contar o número de cidades alcançáveis dentro do limite de distância
            numeroCidadesAlcancaveis = 0
            for d in distancias:
                if d <= distanceThreshold:
                    numeroCidadesAlcancaveis += 1
            
            # Verificar se é a cidade com o menor número de cidades alcançáveis
            if numeroCidadesAlcancaveis <= menorNumeroCidadesAlcancaveis:
                menorNumeroCidadesAlcancaveis = numeroCidadesAlcancaveis
                cidadeComMaisAlcancaveis = i

        return cidadeComMaisAlcancaveis