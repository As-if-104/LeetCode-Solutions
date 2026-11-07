"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""
import copy
from typing import Optional
class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        # copy_node = copy.deepcopy(node)
        # return copy_node
        if not node:
            return None

        start = node
        stack = [start]
        old_to_new = {}
        old_to_new[start] = Node(val=start.val)

        while stack:
            top_node = stack.pop()

            for nei_node in top_node.neighbors:
                if nei_node not in old_to_new:
                    old_to_new[nei_node] = Node(val=nei_node.val)
                    stack.append(nei_node)
        
        for old_node, new_node in old_to_new.items():
            for nei_node in old_node.neighbors:
                new_node.neighbors.append(old_to_new[nei_node])
        
        return old_to_new[start]
