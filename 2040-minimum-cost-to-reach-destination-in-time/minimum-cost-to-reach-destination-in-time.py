class Solution:
    def minCost(self, maxTime: int, edges: list[list[int]], passingFees: list[int]) -> int:
        INF = float('inf')
        n = len(passingFees)

        adj = [[] for _ in range(n)]

        for edge in edges:
            u, v, t = edge
            adj[u].append((v, t))
            adj[v].append((u, t))

        distance = [[INF] * (maxTime + 1) for _ in range(n)]
        distance[0][0] = passingFees[0]

        pq = [(passingFees[0], 0, 0)]

        while pq:
            cost, u, time_used = heapq.heappop(pq)

            if u == n-1:
                return cost

            if cost > distance[u][time_used]:
                continue

            for v, t in adj[u]:
                new_time = time_used + t
                if new_time > maxTime:
                    continue
                
                new_cost = cost + passingFees[v]

                if new_cost < distance[v][new_time]:
                    distance[v][new_time] = new_cost
                    heapq.heappush(pq, (new_cost, v, new_time))

        return -1