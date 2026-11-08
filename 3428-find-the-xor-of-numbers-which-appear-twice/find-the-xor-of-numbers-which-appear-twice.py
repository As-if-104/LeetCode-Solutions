class Solution:
    def duplicateNumbersXOR(self, nums: List[int]) -> int:
        # freq = {}

        # for num in nums:
        #     if num not in freq:
        #         freq[num] = 1
        #     else:
        #         freq[num] += 1

        # ans = []
        # for num in freq:
        #     if freq[num] == 2:
        #         ans.append(num)
        
        # res = 0
        # if len(ans) > 0:
        #     for num in ans:
        #         res ^= num
        #     return res
        # else:
        #     return 0

        seen = set()
        result = 0

        for num in nums:
            if num in seen:
                result ^= num
            else:
                seen.add(num)
        
        return result