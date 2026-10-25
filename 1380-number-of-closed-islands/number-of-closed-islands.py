class Solution:
    def closedIsland(self, grid: list[list[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        visit = set()

        def dfs(i, j):
            if i < 0 or i >= rows or j < 0 or j >= cols:
                return 0
            if grid[i][j] == 1 or (i, j) in visit:
                return 1

            visit.add((i, j))

            return min(dfs(i+1, j), dfs(i, j+1), dfs(i-1, j), dfs(i, j-1))
        
        num_closed_islands = 0
        for i in range(rows):
            for j in range(cols):
                if not grid[i][j] and (i, j) not in visit:
                    num_closed_islands += dfs(i, j)

        return num_closed_islands
