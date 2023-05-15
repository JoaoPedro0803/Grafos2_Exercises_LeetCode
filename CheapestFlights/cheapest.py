import heapq

class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        # Criando o grafo com lista de adjacência
        graph = [[] for _ in range(n)]
        for u, v, w in flights:
            graph[u].append((v, w))

        # Criando o heap mínimo com tuplas (custo, paradas, nó)
        pq = [(0, 0, src)]

        # Criando dicionário para armazenar o menor custo atual para cada nó e número de paradas realizadas
        cost = {}

        while pq:
            # Retirando o nó de menor custo do heap
            curr_cost, curr_stops, curr_node = heapq.heappop(pq)

            # Se o nó atual for o destino, retorna o custo atual
            if curr_node == dst:
                return curr_cost

            # Se o número de paradas realizadas até o momento for maior do que k, ignoramos a aresta
            if curr_stops > k:
                continue

            # Percorrendo todas as arestas saindo do nó atual
            for next_node, edge_cost in graph[curr_node]:
                # Calculando o custo total do caminho até o próximo nó
                total_cost = curr_cost + edge_cost

                # Atualizando o custo atual se o novo custo for menor
                if next_node not in cost or (total_cost, curr_stops + 1) < cost[next_node]:
                    cost[next_node] = (total_cost, curr_stops + 1)
                    heapq.heappush(pq, (total_cost, curr_stops + 1, next_node))

        # Não há caminho para dst
        return -1
    
# https://leetcode.com/problems/cheapest-flights-within-k-stops/description/