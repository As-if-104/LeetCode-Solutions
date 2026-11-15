class Solution:
    def toHex(self, num: int) -> str:
        if num == 0:
            return "0"

        # Convert to unsigned 32-bit representation for negatives
        num &= 0xFFFFFFFF

        hex_chars = "0123456789abcdef"
        result = []

        while num > 0:
            result.append(hex_chars[num & 0xF])
            num >>= 4

        return "".join(reversed(result))