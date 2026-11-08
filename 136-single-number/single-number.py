class Solution:
    def singleNumber(self, nums: list[int]) -> int:
        # freq = {}

        # for num in nums:
        #     if num in freq:
        #         freq[num] += 1
        #     else:
        #         freq[num] = 1
        
        # for num in freq:
        #     if freq[num] == 1:
        #         return num

        res = 0

        for num in nums:
            res ^= num
        
        return res