from collections import defaultdict
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        
        # This is a graph cycle-detection problem
        # If we come back to a node with visit value 1, then there is a cycle

        # Tracks the node states. 0: Unvisited, 1: Visiting, 2: Visited
        state_map = defaultdict(int)

        # Now, build an adjacency list mapping prerequisites. No prereq: needs prereq
        adj = defaultdict(list)
        for p in prerequisites:
            adj[p[1]].append(p[0])

        def dfs(node):
            # Reached the end, no loops!
            if node not in adj:
                return True

            # Already visited this node during the current run, so there's a cycle
            if state_map[node] == 1:
                return False
            elif state_map[node] == 0:
                # Set it to visiting
                state_map[node] = 1
            else:
                return True

            for n in adj[node]:
                if not dfs(n):
                    return False

            state_map[node] = 2

            return True


        for c in range(numCourses):
            if not dfs(c):
                return False

        return True

        

            

            

            



            


