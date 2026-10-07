class Solution:
    def twoSum(self, numbers: list[int], target: int) -> list[int]:
        # n = len(numbers)

        # for i in range(n):
        #     for j in range(i+1, n):
        #         if numbers[i] + numbers[j] == target:
        #             return [i+1, j+1]
        
        # return [0, 0]

        left, right = 0, len(numbers) - 1

        while left < right:
            total = numbers[left] + numbers[right]

            if total == target:
                return [left + 1, right + 1]
            elif total > target:
                right -= 1
            else:
                left += 1
        
        return [0, 0]