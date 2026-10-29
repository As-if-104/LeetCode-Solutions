class Solution:
    def findLUSlength(self, strs: list[str]) -> int:
        strs.sort(key=len, reverse=True)

        def is_subsequence(s, t):
            it = iter(t)
            return all(ch in it for ch in s)

        for i, s in enumerate(strs):
            if not any(is_subsequence(s, strs[j]) for j in range(len(strs)) if j != i):
                return len(s)
        
        return -1