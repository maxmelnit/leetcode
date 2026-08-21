"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""
from collections import defaultdict
class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        
        if not node:
            return None
            
        node_map = defaultdict(Node)

        def dfs(node):

            # Means we've already seen this node, so return the existing copy instead of
            # making a new one
            if node in node_map:
                return node_map[node]

            # Deep copy of the current node, and put it in hashmap
            clone = Node(node.val)
            node_map[node] = clone

            for n in node.neighbors:
                clone.neighbors.append(dfs(n))

            return clone

        return dfs(node)



