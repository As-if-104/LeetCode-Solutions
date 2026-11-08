class Solution:
    def calPoints(self, operations: list[str]) -> int:
        result = []

        for op in operations:
            if op == 'C':
                result.pop()
            elif op == 'D':
                result.append(2 * result[-1])
            elif op == '+':
                result.append(result[-1] + result[-2])
            else:
                result.append(int(op))
        
        return sum(result)