class Solution:
    def isValid(self, s: str) -> bool:
        if len(s) % 2 != 0:
            return False

        hash_map = {')': '(', '}': '{', ']': '['}
        stack = []

        for c in s:
            if c not in hash_map:
                stack.append(c)
            else:
                if not stack:
                    return False
                else:
                    popped = stack.pop()
                    if popped != hash_map[c]:
                        return False
        
        return not stack