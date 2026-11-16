class Solution:
    def digitSum(self, s: str, k: int) -> str:
        while len(s) > k:
            new_s = ""

            for i in range(0, len(s), k):
                chunk = s[i:i+k]
                digit_sum = sum(int(c) for c in chunk)
                new_s += str(digit_sum)

            s = new_s
            
        return s