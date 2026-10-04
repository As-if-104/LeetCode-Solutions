class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        # counter = defaultdict(int)
        counter = {}
        balloon = "balloon"

        for c in text:
            if c in counter:
                counter[c] += 1
            else:
                counter[c] = 1
            
        if any(c not in counter for c in balloon):
            return 0
        else:
            return min(counter['b'], counter['a'], counter['l']//2, counter['o']//2, counter['n'])