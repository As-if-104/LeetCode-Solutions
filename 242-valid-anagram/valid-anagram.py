from collections import Counter
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        # s_sort = sorted(s)
        # t_sort = sorted(t)

        # return s_sort == t_sort

        return Counter(s) == Counter(t)