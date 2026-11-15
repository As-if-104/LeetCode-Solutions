class Solution:
    def validDigit(self, n: int, x: int) -> bool:
        num = str(n)
        found = False

        for ch in num:
            if int(ch) == x:
                found = True
        
        if int(num[:1]) == x:
            return False
        
        return found