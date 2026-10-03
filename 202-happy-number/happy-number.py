class Solution:
    def isHappy(self, n: int) -> bool:
        while n != 1 and n != 4:
            n = self.SumOfSquares(n)
        return n == 1

    def SumOfSquares(self, n: int) -> int:
        total_sum = 0

        while n>0:
            temp = n%10
            total_sum += temp*temp
            n = n//10
        
        return total_sum
