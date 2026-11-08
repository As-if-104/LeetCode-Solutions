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

        n = set(nums)

        ideal_total = sum(n) * 3
        real_total = sum(nums)

        return (ideal_total - real_total) // 2