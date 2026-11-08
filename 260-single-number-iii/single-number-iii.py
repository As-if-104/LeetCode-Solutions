class Solution:
    def singleNumber(self, nums: list[int]) -> list[int]:
        freq = {}
        for num in nums:
            if num not in freq:
                freq[num] = 1
            else:
                freq[num] += 1

        ans = []
        for num in freq:
            if freq[num] == 1:
                ans.append(num)
        
        return ans