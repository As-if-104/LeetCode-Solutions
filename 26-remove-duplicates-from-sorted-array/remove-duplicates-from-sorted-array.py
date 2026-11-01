class Solution:
    def removeDuplicates(self, nums: list[int]) -> int:
        visit = set()
        k = 0

        for num in nums:
            if num not in visit:
                visit.add(num)
                nums[k] = num
                k += 1
        
        return k