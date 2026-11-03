class Solution:
    def tribonacci(self, n: int) -> int:
        # if n <= 1:
        #     return n
        
        # prev3 = 0
        # prev2 = 1
        # prev1 = 1

        # for _ in range(3, n+1):
        #     current = prev3 + prev2 + prev1
        #     prev3 = prev2
        #     prev2 = prev1
        #     prev1 = current
        
        # return prev1

        if n <= 1:
            return n
        if n == 2:
            return 1
        
        dp = [0] * (n+1)
        dp[0] = 0
        dp[1] = 1
        dp[2] = 1

        for i in range(3, n+1):
            dp[i] = dp[i-1] + dp[i-2] + dp[i-3]
        
        return dp[n]