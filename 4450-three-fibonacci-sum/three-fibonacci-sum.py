class Solution:
    def threeFibonacciSum(self, n: int) -> bool:
        dp = [0, 1, 1]

        while dp[-1] + dp[-2] + dp[-3] <= n:
            dp.append(dp[-1] + dp[-2])
        
        for i in range(len(dp) - 2):
            if dp[i] + dp[i+1] + dp[i+2] == n:
                return True
        
        return False