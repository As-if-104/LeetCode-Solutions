class Solution:
    def rob(self, nums: list[int]) -> int:
        # prev2, prev1 = 0, 0

        # for money in nums:
        #     prev2, prev1 = prev1, max(prev1, prev2 + money)
        
        # return prev1

        n = len(nums)

        if n == 0:
            return 0
        if n == 1:
            return nums[0]
        
        dp = [0] * (n+1)
        dp[1] = nums[0]

        for i in range(2, n+1):
            dp[i] = max(dp[i-1], nums[i-1] + dp[i-2])
        
        return dp[n]
        

