import heapq

class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        N = len(grid)
        directions = [[0, 1], [0, -1], [1, 0], [-1, 0]]

        # Criando o grafo com lista de adjacência
        graph = {}
        for i in range(N):
            for j in range(N):
                node = i * N + j
                graph[node] = []
                for dr, dc in directions:
                    ni, nj = i + dr, j + dc
                    if 0 <= ni < N and 0 <= nj < N:
                        neighbor = ni * N + nj
                        weight = max(grid[i][j], grid[ni][nj])
                        graph[node].append((neighbor, weight))

        # Criando dicionário para armazenar a distância mínima para cada nó
        dist = {node: float('inf') for node in range(N*N)}
        dist[0] = grid[0][0]

        # Criando heap mínimo com tuplas (distância, nó)
        pq = [(dist[0], 0)]

        while pq:
            curr_dist, node = heapq.heappop(pq)

            if node == N*N - 1:
                return curr_dist

            if curr_dist > dist[node]:
                continue

            for neighbor, weight in graph[node]:
                total_dist = max(curr_dist, weight)

                if total_dist < dist[neighbor]:
                    dist[neighbor] = total_dist
                    heapq.heappush(pq, (total_dist, neighbor))

        return -1


# https://leetcode.com/problems/swim-in-rising-water/description/