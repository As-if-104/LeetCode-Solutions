class Solution:
    def countDominantElements(self, nums: list[int]) -> int:
        n = len(nums)
        if n == 1:
            return 1

        count = 0

        for i in range(n):
            if i == 0:
                if nums[i] >= nums[i+1]:
                    count += 1
            elif i == n-1:
                if nums[i] >= nums[i-1]:
                    count += 1
            else:
                if nums[i] * 2 >= (nums[i-1] + nums[i+1]):
                    count += 1

        return count