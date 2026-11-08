class Solution:
    def nearestValidPoint(self, x: int, y: int, points: list[list[int]]) -> int:
        min_dist = float('inf')
        best_index = -1

        for i in range(len(points)):
            px, py = points[i]

            if px == x or py == y:
                distance = abs(px - x) + abs(py - y)

                if distance < min_dist:
                    min_dist = distance
                    best_index = i
        
        return best_index