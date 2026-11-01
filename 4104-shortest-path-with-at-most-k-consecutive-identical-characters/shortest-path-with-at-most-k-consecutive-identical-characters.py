class Solution:
    def shortestPath(self, n: int, edges: List[List[int]], labels: str, k: int) -> int:
        graph = [[] for _ in range(n)]
        for edge in edges:
            u, v, w = edge
            graph[u].append((v, w))

        INF = float('inf')

        dist = [[INF] * (k+1) for _ in range(n)]
        dist[0][1] = 0

        pq = [(0, 0, 1)]

        while pq:
            cost, u, count = heapq.heappop(pq)

            if u == n-1:
                return cost
            
            if cost > dist[u][count]:
                continue
            
            for v, w in graph[u]:
                new_cost = cost + w
                if labels[v] == labels[u]:
                    new_count = count + 1
                    if new_count > k:
                        continue
                else:
                    new_count = 1

                if new_cost < dist[v][new_count]:
                    dist[v][new_count] = new_cost
                    heapq.heappush(pq, (new_cost, v, new_count))
        
        return -1