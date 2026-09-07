from collections import defaultdict
class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        
        # Empty tree is a valid tree
        if not n:
            return True

        adj = defaultdict(list)

        # Building the adjacency list
        for n1, n2 in edges:
            adj[n1].append(n2)
            adj[n2].append(n1)

        visited = set()

        def dfs(node, parent):

            # Already seen this node
            if node in visited:
                return False

            # Otherwise mark this node as visited
            visited.add(node)

            # Nowhere left to go
            if adj[node] == [parent]:
                return True

            # Repeat for the children
            for n in adj[node]:
                if n != parent:
                    if not dfs(n, node): # Node becomes the new parent
                        return False

            return True

        if not dfs(0, -1):
            return False

        # Now check that the graph is actually connected:
        return True if len(visited) == n else False


            