class Solution:
    def numOfSubarrays(self, arr: list[int]) -> int:
        MOD = 10**9 + 7
        even_count = 1
        odd_count = 0
        prefix = 0
        ans = 0

        for x in arr:
            prefix = (prefix + x) % 2

            if prefix == 1:
                ans = (ans + even_count) % MOD
                odd_count += 1
            else:
                ans = (ans + odd_count) % MOD
                even_count += 1
        
        return ans
