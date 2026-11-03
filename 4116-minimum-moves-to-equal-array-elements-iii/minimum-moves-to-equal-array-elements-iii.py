class Solution:
    def minMoves(self, nums: List[int]) -> int:
        n = len(nums)

        max_num = max(nums)

        return sum(abs(max_num - num) for num in nums)