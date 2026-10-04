from collections import Counter
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        # s_sort = sorted(s)
        # t_sort = sorted(t)

        # return s_sort == t_sort

        # return Counter(s) == Counter(t)

        hash_s = {}
        hash_t = {}

        for c in s:
            if c in hash_s:
                hash_s[c] += 1
            else:
                hash_s[c] = 1

        for c in t:
            if c in hash_t:
                hash_t[c] += 1
            else:
                hash_t[c] = 1

        return hash_s == hash_t