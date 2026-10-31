class Solution:
    def findCheapestPrice(self, n: int, flights: list[list[int]], src: int, dst: int, k: int) -> int:
        INF = float('inf')
        distance = [INF] * n
        distance[src] = 0

        for _ in range(k+1):
            temp_dist = distance.copy()

            for flight in flights:
                u, v, w = flight

                if distance[u] != INF and distance[u] + w < temp_dist[v]:
                    temp_dist[v] = distance[u] + w

            distance = temp_dist

        return -1 if distance[dst] == INF else distance[dst]

                