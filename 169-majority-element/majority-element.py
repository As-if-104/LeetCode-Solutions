class Solution:
    def majorityElement(self, nums: list[int]) -> int:
        # nums.sort()

        # n = len(nums)

        # return nums[n // 2]


        # counter = {}

        # for num in nums:
        #     if num in counter:
        #         counter[num] += 1
        #     else:
        #         counter[num] = 1
        
        # max_count = -1
        # ans = -1

        # for key, value in counter.items():
        #     if value > max_count:
        #         max_count = value
        #         ans = key

        # return ans

        ans = -1
        count = 0

        for num in nums:
            if count == 0:
                ans = num
            
            if ans == num:
                count += 1
            else:
                count -= 1
        
        return ans