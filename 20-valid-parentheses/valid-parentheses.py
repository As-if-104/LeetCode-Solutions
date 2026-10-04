class Solution:
    def isValid(self, s: str) -> bool:
        if len(s)%2 != 0:
            return False
        
        # stack = [""] * len(s)
        # head = 0

        # for c in s:
        #     if c == "(":
        #         stack[head] = ")"
        #         head += 1
        #     elif c == "{":
        #         stack[head] = "}"
        #         head += 1
        #     elif c == "[":
        #         stack[head] = "]"
        #         head += 1
        #     else:
        #         if head == 0:
        #             return False
                
        #         head -= 1

        #         if stack[head] != c:
        #             return False
        
        # return head == 0

        hashmap = {")":"(", "}":"{", "]":"["}
        stack = []

        for c in s:
            if c not in hashmap:
                stack.append(c)
            else:
                if not stack:
                    return False
                else:
                    popped = stack.pop()
                    if popped != hashmap[c]:
                        return False
        
        return not stack

