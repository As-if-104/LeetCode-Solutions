class Solution:
    def findOrder(self, numCourses: int, prerequisites: list[list[int]]) -> list[int]:
        g = defaultdict(list)
        order = []

        for u, v in prerequisites:
            g[u].append(v)
        
        UNVISITED = 0
        VISITING = 1
        VISITED = 2

        states = [UNVISITED] * numCourses

        def dfs(node):
            state = states[node]

            if state == VISITING:
                return False
            if state == VISITED:
                return True
            
            states[node] = VISITING

            for nei in g[node]:
                if not dfs(nei):
                    return False
            
            states[node] = VISITED
            order.append(node)

            return True

        for i in range(numCourses):
            if not dfs(i):
                return []
        
        return order
