from collections import defaultdict
class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        
        if not n:
            return 0

        count = 0
        seen = set()
        adj = defaultdict(list)

        # Make the adjacency list
        for n1, n2 in edges:
            adj[n1].append(n2)
            adj[n2].append(n1)

        def dfs(node):

            if node in seen:
                return

            seen.add(node)

            for n in adj[node]:
                dfs(n)

        for i in range(n):
            if not i in seen:
                dfs(i)
                count += 1
        
        return count
           

            

