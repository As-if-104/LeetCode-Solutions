from typing import List

class Solution:
    def createGrid(self, m: int, n: int, k: int) -> List[str]:
        # Templates: (height, width, grid) with exactly k monotone paths,
        # bottom-right cell free (entry for corridor extension).
        special_3x3 = ["..#",
                       "...",
                       "#.."]
        
        candidates_by_k = {
            1: [(1, 1, ["."])],
            2: [(2, 2, ["..", ".."])],
            3: [(2, 3, ["...", "..."]),
                (3, 2, ["..", "..", ".."])],
            4: [(2, 4, ["....", "...."]),
                (4, 2, ["..", "..", "..", ".."]),
                (3, 3, special_3x3)],
        }
        
        def embed(a, b, tpl):
            g = [['#'] * n for _ in range(m)]
            for i in range(a):
                for j in range(b):
                    g[i][j] = tpl[i][j]
            # Corridor: right along row a-1 (cols b..n-1), then down col n-1 (rows a..m-1)
            for j in range(b, n):
                g[a - 1][j] = '.'
            for i in range(a, m):
                g[i][n - 1] = '.'
            return [''.join(row) for row in g]
        
        for (a, b, tpl) in candidates_by_k[k]:
            if a <= m and b <= n:
                return embed(a, b, tpl)
        
        return []