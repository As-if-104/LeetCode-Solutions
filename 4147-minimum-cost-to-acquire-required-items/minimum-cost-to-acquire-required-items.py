class Solution:
    def minimumCost(self, cost1: int, cost2: int, costBoth: int, need1: int, need2: int) -> int:
        def calc(k):
            r1 = max(0, need1 - k)
            r2 = max(0, need2 - k)
            return k * costBoth + r1 * cost1 + r2 * cost2
        
        candidates = {0, need1, need2, min(need1, need2), max(need1, need2)}
        return min(calc(k) for k in candidates)