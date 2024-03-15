def unique_paths_dfs(grid):
    def dfs(x, y):
        if x < 0 or y < 0 or x >= len(grid) or y >= len(grid[0]) or grid[x][y] == 0 or visited[x][y]:
            return 0
        if (x, y) == (len(grid)-1, len(grid[0])-1):
            return 1
        
        visited[x][y] = True
        
        right_paths = dfs(x, y + 1)
        down_paths = dfs(x + 1, y)
        
        # visited[x][y] = False
        
        return right_paths + down_paths
    
    if not grid or not grid[0]:
        return 0
    
    visited = [[False] * len(grid[0]) for _ in range(len(grid))]
    return dfs(0, 0)

# Test the function with the given grid
grid = [[1,1,1,0,0],[1,0,1,0,0],[1,1,1,1,1],[0,0,1,1,1],[0,0,1,1,1]]
print("Number of unique paths without intersecting (using DFS with visit once):", unique_paths_dfs(grid))
