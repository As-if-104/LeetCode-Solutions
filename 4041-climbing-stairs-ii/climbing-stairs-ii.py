class Solution:
    def climbStairs(self, n: int, costs: List[int]) -> int:
        # INF = float('inf')

        # dp = [INF] * (n+1)
        # dp[0] = 0

        # for j in range(1, n+1):
        #     best = INF

        #     for jump in (1, 2, 3):
        #         i = j - jump
        #         if i >= 0:
        #             candidate = dp[i] + costs[j-1] + jump*jump
                    
        #             if candidate < best:
        #                 best = candidate
            
        #     dp[j] = best
        
        # return dp[n]

        f0 = f1 = f2 = 0

        for c in costs:
            f0, f1, f2 = f1, f2, min(f0 + 9, f1 + 4, f2 + 1) + c
        
        return f2