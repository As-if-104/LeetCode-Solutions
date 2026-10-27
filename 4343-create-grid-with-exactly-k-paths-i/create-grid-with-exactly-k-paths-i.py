class Solution:
    def createGrid(self, m: int, n: int, k: int) -> List[str]:
        grid = []

        for i in range(m):
            if i == 0:
                grid.append('.' * n)
            else:
                grid.append('#' * (n-1) + '.')

        if k >= 2:
            if m >= 2 and n >= 2:
                row = list(grid[1])
                row[n-2] = '.'
                grid[1] = ''.join(row)
            else:
                return []
        
        if k >= 3:
            if n >= 3 and n >= m:
                row = list(grid[1])
                row[n-3] = '.'
                grid[1] = ''.join(row)
            elif m >= 3 and m >= n:
                row = list(grid[2])
                row[n-2] = '.'
                grid[2] = ''.join(row)
            else:
                return []

        if k == 4:
            if n >= 4 and n >= m:
                row = list(grid[1])
                row[n-4] = '.'
                grid[1] = ''.join(row)
            elif m >= 4 and m >= n:
                row = list(grid[3])
                row[n-2] = '.'
                grid[3] = ''.join(row)
            elif m == 3 and n == 3:
                return ["..#", "...", "#.."]
            else:
                return []

        return grid