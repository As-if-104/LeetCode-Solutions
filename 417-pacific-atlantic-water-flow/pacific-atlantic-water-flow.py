class Solution:
    def pacificAtlantic(self, heights: list[list[int]]) -> list[list[int]]:
        p_queue = deque()
        p_seen = set()

        a_queue = deque()
        a_seen = set()

        m, n = len(heights), len(heights[0])

        for j in range(n):
            p_queue.append((0, j))
            p_seen.add((0, j))

        for i in range(1, m):
            p_queue.append((i, 0))
            p_seen.add((i, 0))
        
        for i in range(m):
            a_queue.append((i, n-1))
            a_seen.add((i, n-1))

        for j in range(n-1):
            a_queue.append((m-1, j))
            a_seen.add((m-1, j))
        
        def get_coords(que, seen):
            coords = set()

            while que:
                i, j = que.popleft()
                for i_off, j_off in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                    new_i, new_j = i + i_off, j + j_off

                    if 0 <= new_i < m and 0 <= new_j < n and heights[new_i][new_j] >= heights[i][j] and (new_i, new_j) not in seen:
                        seen.add((new_i, new_j))
                        que.append((new_i, new_j))
        
        get_coords(p_queue, p_seen)
        get_coords(a_queue, a_seen)

        return list(p_seen.intersection(a_seen))

