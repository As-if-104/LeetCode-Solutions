class Solution:
    def searchMatrix(self, matrix: list[list[int]], target: int) -> bool:
        row = len(matrix)
        col = len(matrix[0])
        n = row * col

        left, right = 0, n - 1

        while left <= right:
            mid = (left + right) // 2

            row_index = mid // col
            col_index = mid % col

            value = matrix[row_index][col_index]

            if value == target:
                return True
            elif value > target:
                right = mid - 1
            else:
                left = mid + 1
        
        return False