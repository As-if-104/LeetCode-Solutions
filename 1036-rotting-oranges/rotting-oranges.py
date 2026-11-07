class Solution:
    def orangesRotting(self, grid: list[list[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        num_fresh_oranges = 0
        num_minutes = -1
        queue = deque()

        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 1:
                    num_fresh_oranges += 1
                elif grid[i][j] == 2:
                    queue.append((i, j))
        
        if num_fresh_oranges == 0:
            return 0
        
        while queue:
            queue_size = len(queue)
            num_minutes += 1

            for _ in range(queue_size):
                i, j = queue.popleft()

                for r, c in [(i, j+1), (i+1, j), (i-1, j), (i, j-1)]:
                    if 0 <= r < rows and 0 <= c < cols and grid[r][c] == 1:
                        grid[r][c] = 2
                        num_fresh_oranges -= 1
                        queue.append((r, c))

        if num_fresh_oranges == 0:
            return num_minutes
        else:
            return -1



