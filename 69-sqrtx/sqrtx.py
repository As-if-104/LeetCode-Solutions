class Solution:
    def mySqrt(self, x: int) -> int:
        # if x < 0:
        #     return ValueError("Wrong!")
        # if x == 0:
        #     return 0.0
        # if x == 1:
        #     return 1.0

        # guess = x
        # epsilon = 1e-10

        # while True:
        #     next_guess = 0.5 * (guess + x/guess)

        #     if abs(guess-next_guess) < epsilon:
        #         return next_guess
            
        #     guess = next_guess

        if x < 2:
            return x

        left, right = 2, x//2

        while left <= right:
            pivot = left + (right-left)//2
            num = pivot*pivot

            if num < x:
                left = pivot+1
            elif num > x:
                right = pivot-1
            else:
                return pivot
        
        return right