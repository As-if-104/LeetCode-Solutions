class Solution:
    def search(self, nums: list[int], target: int) -> int:
        left, right = 0, len(nums) - 1

        while left < right:
            mid = (left + right) // 2

            if nums[mid] > nums[right]:
                left = mid + 1
            else:
                right = mid
        
        min_index = left

        if min_index == 0:
            left, right = 0, len(nums) - 1
        elif target >= nums[0] and target <= nums[min_index - 1]:
            left, right = 0, min_index - 1
        else:
            left, right = min_index, len(nums) - 1
        
        while left <= right:
            mid = (left + right) // 2

            if nums[mid] == target:
                return mid
            elif nums[mid] > target:
                right = mid - 1
            else:
                left = mid + 1
        
        return -1
