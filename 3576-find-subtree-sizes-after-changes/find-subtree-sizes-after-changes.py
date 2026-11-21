class Solution:
    def findSubtreeSizes(self, parent, s):
        n = len(parent)
        
        # Build original children list
        children = [[] for _ in range(n)]
        for i in range(1, n):
            children[parent[i]].append(i)
        
        # Step 1: DFS to find new parent for each node
        new_parent = parent[:]  # default: keep original
        last_seen = {}  # char -> deepest ancestor node with that char
        
        def dfs(x):
            old = last_seen.get(s[x], -1)  # save previous value for backtrack
            if x != 0 and old != -1:
                new_parent[x] = old  # re-parent to closest same-char ancestor
            last_seen[s[x]] = x
            for c in children[x]:
                dfs(c)
            # backtrack
            if old == -1:
                del last_seen[s[x]]
            else:
                last_seen[s[x]] = old
        
        dfs(0)
        
        # Step 2: Build new tree and compute subtree sizes
        new_children = [[] for _ in range(n)]
        for i in range(1, n):
            new_children[new_parent[i]].append(i)
        
        size = [1] * n
        def dfs2(x):
            for c in new_children[x]:
                dfs2(c)
                size[x] += size[c]
        
        dfs2(0)
        return size