import heapq

class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        # Cria o grafo
        graph = {}
        for u, v, w in times:
            if u not in graph:
                graph[u] = []
            graph[u].append((v, w))
        
        # Inicializa as distâncias com infinito
        dist = {node: float('inf') for node in range(1, n+1)}
        dist[k] = 0
        
        # Usa um heap mínimo para escolher o nó com a menor distância
        heap = [(0, k)]
        
        # Percorre todos os nós usando o algoritmo de Dijkstra
        while heap:
            curr_dist, node = heapq.heappop(heap)
            if curr_dist > dist[node]:
                continue
            if node in graph:
                for neighbor, weight in graph[node]:
                    distance = curr_dist + weight
                    if distance < dist[neighbor]:
                        dist[neighbor] = distance
                        heapq.heappush(heap, (distance, neighbor))
        
        # Verifica se todos os nós foram alcançados
        max_dist = max(dist.values())
        if max_dist == float('inf'):
            return -1
        return max_dist
    
# https://leetcode.com/problems/network-delay-time/description/