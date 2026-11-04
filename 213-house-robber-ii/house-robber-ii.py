class Solution:
    def rob(self, nums: list[int]) -> int:
        n = len(nums)

        if n == 0:
            return 0
        if n == 1:
            return nums[0]
        if n == 2:
            return max(nums[0], nums[1])

        def house_robber(arr: list[int]) -> int:
            prev2, prev1 = 0, 0

            for money in arr:
                prev2, prev1 = prev1, max(prev1, prev2 + money)
            
            return prev1
        
        return max(house_robber(nums[1:]), house_robber(nums[:-1]))