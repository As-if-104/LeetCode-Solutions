class Solution:
    def targetIndices(self, nums: list[int], target: int) -> list[int]:
        nums.sort()

        seen = []

        for i in range(len(nums)):
            if nums[i] == target and i not in seen:
                seen.append(i)
        
        return seen