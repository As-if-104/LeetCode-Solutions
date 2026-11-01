class Solution:
    def applyOperations(self, nums: list[int]) -> list[int]:
        n = len(nums)
        k = 0

        for i in range(n-1):
            if nums[i] == nums[i+1] and nums[i] != 0:
                nums[i] *= 2
                nums[i+1] = 0
        
        for num in nums:
            if num != 0:
                nums[k] = num
                k += 1
        
        for i in range(k, n):
            nums[i] = 0
        
        return nums