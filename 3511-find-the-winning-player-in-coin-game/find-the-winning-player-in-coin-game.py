class Solution:
    def winningPlayer(self, x: int, y: int) -> str:
        count = 0

        while x > 0 and y > 3:
            x -= 1
            y -= 4
            count += 1
        
        return "Alice" if count % 2 == 1 else "Bob"