class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        # def recurse(i, j):
        #     if i == len(text1) or j == len(text2):
        #         return 0
            
        #     if text1[i] == text2[j]:
        #         return 1 + recurse(i+1, j+1)
        #     else:
        #         return max(recurse(i+1, j), recurse(i, j+1))

        # return recurse(0, 0)

        m, n = len(text1), len(text2)

        dp = [[0] * (n+1) for _ in range(m+1)]

        for i in range(m):
            for j in range(n):
                if text1[i] == text2[j]:
                    dp[i][j] = 1 + dp[i-1][j-1]
                else:
                    dp[i][j] = max(dp[i-1][j], dp[i][j-1])
        
        return dp[m-1][n-1]