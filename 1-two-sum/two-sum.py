class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        n = len(nums)

        # for i in range(n):
        #     for j in range(i+1, n):
        #         if nums[i] + nums[j] == target:
        #             return [i, j]
        
        # return []

        hashmap = {}

        for i in range(n):
            hashmap[nums[i]] = i

        for i in range(n):
            y = target - nums[i]

            if y in hashmap and hashmap[y] != i:
                return [i, hashmap[y]]