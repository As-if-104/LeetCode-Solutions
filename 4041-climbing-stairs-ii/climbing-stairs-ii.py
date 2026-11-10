class Solution:
    def climbStairs(self, n: int, costs: List[int]) -> int:
        INF = float('inf')

        dp = [INF] * (n+1)
        dp[0] = 0

        for j in range(1, n+1):
            best = INF

            for jump in (1, 2, 3):
                i = j - jump
                if i >= 0:
                    candidate = dp[i] + costs[j-1] + jump*jump
                    
                    if candidate < best:
                        best = candidate
            
            dp[j] = best
        
        return dp[n]