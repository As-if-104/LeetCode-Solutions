class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        counter = defaultdict(int)
        ballon = "ballon"

        for c in text:
            if c in ballon:
                counter[c] += 1
            
        if any(c not in counter for c in ballon):
            return 0
        else:
            return min(counter['b'], counter['a'], counter['l']//2, counter['o']//2, counter['n'])