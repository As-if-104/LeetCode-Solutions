class Solution:
    def smallestEqual(self, nums: list[int]) -> int:
        # result = []

        # for i in range(len(nums)):
        #     if i % 10 == nums[i]:
        #         result.append(i)
        
        # return min(result) if result else -1

        for index, num in enumerate(nums):
            if index % 10 == num:
                return index
        
        return -1