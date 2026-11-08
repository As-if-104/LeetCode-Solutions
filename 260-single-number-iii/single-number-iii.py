class Solution:
    def singleNumber(self, nums: list[int]) -> list[int]:
        # freq = {}
        # for num in nums:
        #     if num not in freq:
        #         freq[num] = 1
        #     else:
        #         freq[num] += 1

        # ans = []
        # for num in freq:
        #     if freq[num] == 1:
        #         ans.append(num)
        
        # return ans

        # hash_set = set()

        # for num in nums:
        #     if num in hash_set:
        #         hash_set.remove(num)
        #     else:
        #         hash_set.add(num)
        
        # return list(hash_set)

        xor_sum = 0

        for num in nums:
            xor_sum ^= num
        
        diff_bit = xor_sum & -xor_sum

        x, y = 0, 0

        for num in nums:
            if num & diff_bit:
                x ^= num
            else:
                y ^= num
        
        return [x, y]