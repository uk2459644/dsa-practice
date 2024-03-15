
grid = [
    ["b","a","c"],
    ["c","a","c"],
    ["d","d","c"],
    ["b","c","c"]]

m,n=len(grid),len(grid[0])

visited = [[0 for _ in range(n)] for _ in range(m)]

def dfs(i,j,color,dir):
    if visited[i][j]==1:
        return False
    
    if visited[i][j]==-1:
        return True
    
    if dir != "D" and i<m-1 and grid[i+1][j]==color:
        if dfs(i+1,j,color,'D'):
            return True
    
    if dir != 'U' and i>0 and grid[i-1][j]==color:
        if dfs(i-1,j,color,'D'):
            return True
    
    if dir != 'L' and j<n-1 and grid[i][j+1]==color:
        if dfs(i,j+1,color,'R'):
            return True
    
    if dir != 'R' and j>0 and grid[i][j-1]==color:
        if dfs(i,j-1,color,'L'):
            return True
    
    visited[i][j]=1

    return False


