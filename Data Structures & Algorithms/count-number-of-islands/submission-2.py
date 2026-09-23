class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        
        rows = len(grid)
        cols = len(grid[0])
        island_count = 0

        # We're gonna 'sink the island'.

        def dfs(i, j):
            # Base case (when we do recursion out of bounds) or we find a 0 (skip dfs for that one)
            if i < 0 or i >= rows or j < 0 or j >= cols or grid[i][j] == '0':
                return

            # Now we know we are both in bounds, and the (i, j)th index is a 1
            # First, flip that 1 to a 0
            grid[i][j] = '0'
            
            # Now, we want to explore all of the '1' neighbours of this node
            dfs(i + 1, j)
            dfs(i - 1, j)
            dfs(i, j + 1)
            dfs(i, j - 1)

        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == '1': # Avoid unnecessary work on 0 cells
                    island_count += 1 # Each time we sink a new island, we increase count
                    dfs(i, j)
        
        return island_count

