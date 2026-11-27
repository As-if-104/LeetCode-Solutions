class Solution:
    def maximumSaleItems(self, items: List[List[int]], budget: int) -> int:
        n = len(items)
        factors = [it[0] for it in items]
        prices  = [it[1] for it in items]

        # freeCount[i] = number of j != i with factors[i] dividing factors[j]
        freeCount = [0] * n
        for i in range(n):
            fi = factors[i]
            cnt = 0
            for j in range(n):
                if i != j and factors[j] % fi == 0:
                    cnt += 1
            freeCount[i] = cnt

        # 0/1 knapsack: choose which types get at least one purchase
        NEG = -10**9
        dp = [NEG] * (budget + 1)
        dp[0] = 0
        for i in range(n):
            cost = prices[i]
            val  = 1 + freeCount[i]
            for b in range(budget, cost - 1, -1):
                if dp[b - cost] != NEG:
                    dp[b] = max(dp[b], dp[b - cost] + val)

        minPrice = min(prices)
        ans = 0
        for b in range(budget + 1):
            if dp[b] != NEG:
                extra = (budget - b) // minPrice
                ans = max(ans, dp[b] + extra)

        return ans