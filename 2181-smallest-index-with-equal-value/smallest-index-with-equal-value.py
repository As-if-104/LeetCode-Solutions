class Solution:
    def smallestEqual(self, nums: list[int]) -> int:
        result = []

        for i in range(len(nums)):
            if i % 10 == nums[i]:
                result.append(i)
        
        return min(result) if result else -1