class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        # s_list = list(s)
        # t_list = list(t)

        # return s_list.sort() == t_list.sort()

        s_sort = sorted(s)
        t_sort = sorted(t)

        return s_sort == t_sort