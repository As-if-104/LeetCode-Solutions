class Solution:
    def minCostClimbingStairs(self, cost: list[int]) -> int:
        n = len(cost)

        # dp = [0] * (n+1)

        # for i in range(2, n+1):
        #     dp[i] = min(dp[i-2] + cost[i-2], dp[i-1] + cost[i-1])
        
        # return dp[n]

        prev, curr = 0, 0

        for i in range(2, n+1):
            prev, curr = curr, min(cost[i-2] + prev, cost[i-1] + curr)
        
        return curr