class Solution:
    def minimumEffortPath(self, heights: list[list[int]]) -> int:
        rows, cols = len(heights), len(heights[0])

        min_heap = [(0, 0, 0)]
        directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]

        visit = set()

        while min_heap:
            effort, r, c = heapq.heappop(min_heap)

            if (r, c) in visit:
                continue
            visit.add((r, c))

            if (r, c) == (rows-1, cols-1):
                return effort
            
            for dr, dc in directions:
                new_row, new_col = dr + r, dc + c

                if new_row < 0 or new_col < 0 or new_row == rows or new_col == cols or (new_row, new_col) in visit:
                    continue
                    
                new_effort = max(effort, abs(heights[r][c] - heights[new_row][new_col]))
                heapq.heappush(min_heap, (new_effort, new_row, new_col))