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

            return min(dfs(i, j+1), dfs(i+1, j), dfs(i-1, j), dfs(i, j-1))

        num_closed_islands= 0
        for r in range(rows):
            for c in range(cols):
                if not grid[r][c] and (r, c) not in visit:
                    num_closed_islands += dfs(r, c)

        return num_closed_islands