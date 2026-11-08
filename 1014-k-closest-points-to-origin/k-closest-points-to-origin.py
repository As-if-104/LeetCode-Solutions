class Solution:
    def kClosest(self, points: list[list[int]], k: int) -> list[list[int]]:
        max_heap = []

        for i in range(len(points)):
            x, y = points[i]

            dist = x * x + y * y

            heapq.heappush(max_heap, (-dist, x, y))

            if len(max_heap) > k:
                heapq.heappop(max_heap)

        return [[x, y] for (_, x, y) in max_heap]