class Solution:
    def missingNumber(self, nums: list[int]) -> int:
        n = len(nums)

        total_sum = (n*(n+1))//2

        actual_sum = sum(nums)

        missing_number = total_sum - actual_sum

        return missing_number