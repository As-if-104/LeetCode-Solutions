class Solution:
    def minMoves(self, nums: list[int]) -> int:
        # min_value = min(nums)

        # return sum(num - min_value for num in nums)

        return sum(nums) - len(nums) * min(nums)