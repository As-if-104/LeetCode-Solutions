class Solution:
    def maxSelectedElements(self, nums: List[int]) -> int:
        nums.sort()
        dp = {}
        
        for v in nums:
            old_v0 = dp.get((v, 0), 0)
            old_v1 = dp.get((v, 1), 0)
            
            # Keep v as v: extend from v-1
            keep = 1
            keep = max(keep, dp.get((v - 1, 0), 0) + 1)
            keep = max(keep, dp.get((v - 1, 1), 0) + 1)
            
            # Increment v to v+1: extend from v (using OLD values)
            inc = 1
            inc = max(inc, old_v0 + 1)
            inc = max(inc, old_v1 + 1)
            
            dp[(v, 0)] = max(dp.get((v, 0), 0), keep)
            dp[(v + 1, 1)] = max(dp.get((v + 1, 1), 0), inc)
        
        return max(dp.values()) if dp else 0