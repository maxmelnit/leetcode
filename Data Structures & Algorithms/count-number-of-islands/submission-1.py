class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        
        island_count = 0
        grid_rows = len(grid)
        grid_cols = len(grid[0])

        # No grid, no islands
        if not grid:
            return 0

        def dfs(i, j):
            
            if i < 0 or i >= grid_rows or j < 0 or j >= grid_cols or grid[i][j] != '1':
                return

            grid[i][j] = '0'
            dfs(i + 1, j)
            dfs(i - 1, j)
            dfs(i, j + 1)
            dfs(i, j - 1)



        # "Sink the 1's recursively with dfs"
        for i in range(grid_rows):
            for j in range(grid_cols):
                if grid[i][j] == '1':
                    island_count += 1
                    dfs(i, j)

        return island_count
            
            
        
                

