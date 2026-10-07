from collections import deque

class Solution:
    def removeInvalidParentheses(self, s: str) -> list[str]:
        def isValid(expr):
            count = 0

            for c in expr:
                if c not in "()":
                    continue
                if c == "(":
                    count += 1
                elif c == ")":
                    count -= 1
                if count < 0:
                    return False
            return count == 0

        if len(s) == 0:
            return [""]

        visited = set()

        queue = deque()
        queue.append(s)
        visited.add(s)

        found = False
        output = []

        while queue:
            expr = queue.popleft()

            if isValid(expr):
                output.append(expr)
                found = True
            
            if found:
                continue

            for i in range(len(expr)):
                if expr[i] not in '()':
                    continue
                
                candidate = expr[:i] + expr[i+1:]
                if candidate not in visited:
                    queue.append(candidate)
                    visited.add(candidate)
        
        return output if output else [""]