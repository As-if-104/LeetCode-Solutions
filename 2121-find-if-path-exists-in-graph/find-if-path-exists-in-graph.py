class Solution:
    def validPath(self, n: int, edges: list[list[int]], source: int, destination: int) -> bool:
        # 1. DFS with Recursion

        # if source == destination:
        #     return True

        # graph = defaultdict(list)
        # for u, v in edges:
        #     graph[u].append(v)
        #     graph[v].append(u)

        # visit = set()
        # visit.add(source)

        # def dfs(i):
        #     if i == destination:
        #         return True
            
        #     for nei_node in graph[i]:
        #         if nei_node not in visit:
        #             visit.add(nei_node)
        #             if dfs(nei_node):
        #                 return True
            
        #     return False
        
        # return dfs(source)


        # 2. DFS with stack
        
        if source == destination:
            return True
            
        graph = defaultdict(list)    
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)
        
        visit = set()
        visit.add(source)
        stack = [source]

        while stack:
            node = stack.pop()

            if node == destination:
                return True
            
            for nei_node in graph[node]:
                if nei_node not in visit:
                    visit.add(nei_node)
                    stack.append(nei_node)
            
        return False
