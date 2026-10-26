class Solution:
    def countIslands(self, grid: List[List[int]], k: int) -> int:
        rows, cols = len(grid), len(grid[0])

        def dfs(i, j):
            if i < 0 or i >= rows or j < 0 or j >= cols or grid[i][j] == 0:
                return 0
            
            val = grid[i][j]
            grid[i][j] = 0

            return val + dfs(i, j+1) + dfs(i+1, j) + dfs(i-1, j) + dfs(i, j-1)

        count = 0
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] > 0:
                    total = dfs(r, c)
                    if total % k == 0:
                        count += 1
        
        return count