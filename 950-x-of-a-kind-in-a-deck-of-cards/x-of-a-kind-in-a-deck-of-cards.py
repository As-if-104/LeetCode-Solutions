class Solution:
    def hasGroupsSizeX(self, deck: list[int]) -> bool:
        freq = {}

        for card in deck:
            if card in freq:
                freq[card] += 1
            else:
                freq[card] = 1
        
        counts = []

        for card in freq.values():
            counts.append(card)
        
        def gcd(a, b):
            while b != 0:
                a, b = b, a%b
            return a

        g = counts[0]

        for i in range(1, len(counts)):
            g = gcd(g, counts[i])

            if g == 1:
                return False
        
        return g > 1