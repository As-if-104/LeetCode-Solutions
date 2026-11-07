class Solution:
    def minCostConnectPoints(self, points: list[list[int]]) -> int:
        n = len(points)
        visit = set()
        min_heap = [(0, 0)]
        total_cost = 0

        while len(visit) < n:
            distance, index = heapq.heappop(min_heap)
            if index in visit:
                continue
            
            total_cost += distance
            visit.add(index)

            xi, yi = points[index]

            for j in range(n):
                if j not in visit:
                    xj, yj = points[j]
                    nei_points_distance = abs(xi - xj) + abs(yi - yj)
                    heapq.heappush(min_heap, (nei_points_distance, j))
        
        return total_cost