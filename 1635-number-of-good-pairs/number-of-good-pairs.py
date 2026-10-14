class Solution:
    def numIdenticalPairs(self, nums: list[int]) -> int:
        # n = len(nums)
        # good_pairs = 0

        # for i in range(n):
        #     for j in range(i+1, n):
        #         if nums[i] == nums[j]:
        #             good_pairs += 1
        
        # return good_pairs

        n = len(nums)
        good_pairs = 0
        counter = Counter(nums)

        for index, num in enumerate(nums):
            counter[num] -= 1
            good_pairs += counter[num]
        
        return good_pairs