class Solution:
    def sortedSquares(self, nums: list[int]) -> list[int]:
        new_list = []

        for num in nums:
            new_list.append(num ** 2)
        
        new_list.sort()

        return new_list