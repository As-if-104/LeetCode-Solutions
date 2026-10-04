class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        count = 0

        # Time Complexity: O(n*m)

        # for stone in stones:
        #     if stone in jewels:
        #         count += 1
        
        # return count


        # Time Complexity: O(n+m)

        hashset = set(jewels)

        for stone in stones:
            if stone in hashset:
                count += 1

        return count