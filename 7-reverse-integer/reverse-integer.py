class Solution:
    def reverse(self, x: int) -> int:
        INT_MIN, INT_MAX = -2**31, 2**31 - 1
        
        sign = -1 if x < 0 else 1

        reverse = 0
        temp = abs(x)

        while temp > 0:
            digit = temp%10
            temp = temp//10

            if reverse > (INT_MAX - digit) // 10:
                return 0
            reverse = reverse*10 + digit
        
        return sign * reverse