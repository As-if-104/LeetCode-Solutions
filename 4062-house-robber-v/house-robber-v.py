class Solution:
    def rob(self, nums: List[int], colors: List[int]) -> int:
        n = len(nums)
        if n == 0:
            return 0

        dp0 = 0
        dp1 = nums[0]

        for i in range(1, n):
            if colors[i] == colors[i-1]:
                new1 = dp0 + nums[i]
                new0 = max(dp0, dp1)
            else:
                new1 = max(dp0, dp1) + nums[i]
                new0 = max(dp0, dp1)
            
            dp0, dp1 = new0, new1

        return max(dp0, dp1)