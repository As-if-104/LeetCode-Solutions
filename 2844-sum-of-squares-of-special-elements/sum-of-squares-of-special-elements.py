class Solution:
    def sumOfSquares(self, nums: List[int]) -> int:
        n = len(nums)
        total_sum = 0

        for i in range(n+1):
            if n % (i+1) == 0:
                total_sum += nums[i] ** 2

        return total_sum