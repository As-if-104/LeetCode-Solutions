class Solution:
    def minRotations(self, s: str) -> int:
        total = 0
        current = 0

        for ch in s:
            target = int(ch)

            direction = abs(current - target)
            circular = 10 - direction

            total += min(direction, circular)
            current = target
        
        return total