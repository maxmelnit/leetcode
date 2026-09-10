class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:

        # Work outwards in
        visited_pacific = set()
        visited_atlantic = set()
        r = len(heights)
        c = len(heights[0])

        # Two rounds of dfs, one for atlantic and one for pacific
        def dfs(i, j, just_visited, ocean):
            
            # Bounds
            if i < 0 or i >= r or j < 0 or j >= c:
                return

            if ocean == 'p' and (i, j) in visited_pacific:
                return
            elif ocean == 'a' and (i, j) in visited_atlantic:
                return

            # Only want to visit values greater than the current one
            if just_visited > heights[i][j]:
                return
            
            # Depending where we started, add the coords to appropriate set
            if ocean == 'p':
                visited_pacific.add((i, j))
            else:
                visited_atlantic.add((i, j))


            dfs(i + 1, j, heights[i][j], ocean)
            dfs(i - 1, j, heights[i][j], ocean)
            dfs(i, j + 1, heights[i][j], ocean)
            dfs(i, j - 1, heights[i][j], ocean)

        # Pacific
        for i in range(r):
            dfs(i, 0, -1, 'p')
        for j in range(c):
            dfs(0, j, -1, 'p')

        # Atlantic
        for i in range(r):
            dfs(i, c - 1, -1, 'a')
        for j in range(c):
            dfs(r - 1, j, -1, 'a')

        return list(visited_atlantic.intersection(visited_pacific))



            

            





            