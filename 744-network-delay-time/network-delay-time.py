import heapq

def dijkstra(adj: list[list[list[int]]], src: int) -> list[int]:
    vertex = len(adj)
    dist = [float('inf')] * vertex
    dist[src] = 0
    pq = []

    heapq.heappush(pq, (0, src))

    while pq:
        d, u = heapq.heappop(pq)

        if d > dist[u]:
            continue
        
        for x in adj[u]:
            nei = x[0]
            weight = x[1]

            if dist[nei] > weight + d:
                dist[nei] = weight + d
                heapq.heappush(pq, (dist[nei], nei))
    
    return dist

class Solution:
    def networkDelayTime(self, times: list[list[int]], n: int, k: int) -> int:
        adj = [[] for _ in range(n+1)]

        for u, v, w in times:
            adj[u].append((v, w))
        
        distance = dijkstra(adj, k)

        ans = max(distance[1:])

        return -1 if ans == float('inf') else ans