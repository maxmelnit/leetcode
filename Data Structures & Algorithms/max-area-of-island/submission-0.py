class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        
        best = 0
        rows = len(grid)
        cols = len(grid[0])

        # Count the current island size and update the max
        def dfs(i, j):

            # Out of bounds or the grid cell is not part of an island
            if i < 0 or i >= rows or j < 0 or j >= cols or grid[i][j] == 0:
                return 0

            # Sink this piece of the island
            grid[i][j] = 0

            # Do for the rest of the connected cells
            return (dfs(i + 1, j) + dfs(i - 1, j) + dfs(i, j + 1) + dfs(i, j - 1) + 1)

        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 1: # Avoid unnecessary work
                    counted = dfs(i, j)
                    best = max(best, counted) # Update the best island side if required
        
        return best






            