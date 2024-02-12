"""
Method 1 - using DFS Traversal: The idea is to use DFS Traversal to count
the number of island surrounded by water. But we have to keep the track
of the island surrounded by water.

1. Initialize a 2D visited matrix (say vis[][]) to keep the track of traversed
   cell in the given matrix.

2. Perform DFS traversal on all corner of the given matrix and if any element
   has value 1 then marked all the cell with value 1 as visited because it
   cannot be counted in the resultant count.

3. Perform DFS Traversal on all the remaining unvisited cell and if value 
   encountered is 1 then markedthis cell as visited, count this island in the
   resultant count and recursively call DFS for all the 4 directions
   
4. Repeat the above step until all cell with value 1 are not visited.
"""

def dfs(matrix, visited,x,y,n,m):
    # if the land is already visited or there is no land or the coordinates
    # gone out of matrix break function as there will be no islands
    if (x<0 or y<0 or x>=n or y>=m or visited[x][y]==True or matrix[x][y]==0):
        return
    
    # mark land as visited
    visited[x][y]=True
    # traverse to all adjacent elements
    dfs(matrix,visited,x+1,y,n,m)
    dfs(matrix,visited,x,y+1,n,m)
    dfs(matrix,visited,x-1,y,n,m)
    dfs(matrix,visited,x,y-1,n,m)

# function that counts the closed island
def countClosedIsland(matrix,n,m):
    # create boolean 2D visited matrix to keep track of visited cell
    # initially all elements are unnvisited
    visited=[[False for i in range(m)] for j in range(n)]
    # mark visited all lands that are reachable from edge
    for i in range(n):
        for j in range(m):
            # traverse corners
            if ((i*j==0 or i==n-1 or j==m-1) and matrix[i][j]==1 and visited[i][j]==False):
                dfs(matrix,visited,i,j,n,m)
    
    # to store number of closed islands
    result=0
    for i in range(n):
        for j in range(m):
            # if the land not visited hten there will be atleast one closed island
            if (visited[i][j]==False and matrix[i][j]==1):
                result+=1
                dfs(matrix,visited,i,j,n,m)
    
    return result

