class Solution:
    def checkGoodInteger(self, n: int) -> bool:
        digitSum = 0
        squareSum = 0

        for digit in str(n):
            digitSum += int(digit)
            squareSum += int(digit) ** 2
        
        return True if squareSum - digitSum >= 50 else False 
