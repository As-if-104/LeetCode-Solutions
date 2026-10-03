class Solution:
    def myPow(self, x: float, n: int) -> float:
        # return x ** n

        is_negative = n < 0

        n = abs(n)

        result = 1.0
        current_product = x

        while n > 0:
            if n%2 == 1:
                result *= current_product
            
            current_product *= current_product
            n //= 2
        
        return 1.0 / result if is_negative else result