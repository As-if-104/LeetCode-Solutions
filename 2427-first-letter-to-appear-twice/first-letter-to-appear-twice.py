class Solution:
    def repeatedCharacter(self, s: str) -> str:
        seen = []

        for ch in s:
            if ch in seen:
                return ch
            else:
                seen.append(ch)