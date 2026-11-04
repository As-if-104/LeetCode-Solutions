class Solution:
    def findOrder(self, numCourses: int, prerequisites: list[list[int]]) -> list[int]:
        g = defaultdict(list)
        order = []
        indegree = [0] * numCourses
        queue = deque()

        for u, v in prerequisites:
            g[v].append(u)
            indegree[u] += 1
        
        for i in range(numCourses):
            if indegree[i] == 0:
                queue.append(i)
        
        while queue:
            top = queue.popleft()
            order.append(top)

            for nei in g[top]:
                indegree[nei] -= 1
                if indegree[nei] == 0:
                    queue.append(nei)
        
        return order if len(order) == numCourses else []
        
        # UNVISITED = 0
        # VISITING = 1
        # VISITED = 2

        # states = [UNVISITED] * numCourses

        # def dfs(node):
        #     state = states[node]

        #     if state == VISITING:
        #         return False
        #     if state == VISITED:
        #         return True
            
        #     states[node] = VISITING

        #     for nei in g[node]:
        #         if not dfs(nei):
        #             return False
            
        #     states[node] = VISITED
        #     order.append(node)

        #     return True

        # for i in range(numCourses):
        #     if not dfs(i):
        #         return []
        
        # return order
