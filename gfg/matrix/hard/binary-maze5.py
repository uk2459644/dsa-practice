"""
The idea is to use Backtracking. We first mark all adjacent cells of the
as unsafe. Then for each safe cell of first column of the matrix, we move forward
in all allowed directions and recursively checks if they leads to the
destination or not. If destination is found, we update the value of shortest
path else if none of the above solutions work we return from our function.

"""
import sys 

R=12
C=10

# these arrays are used to get row and column number of 4 neighbours 
# of a given cell
rowNum=[-1,0,0,1]
colNum=[0,-1,1,0]

min_dist=sys.maxsize

# a function to check if a given cell (x,y)
# can be visited or not

def isSafe(mat,visited,x,y):
    if (mat[x][y]==0 or visited[x][y]):
        return False
    
    return True

# A function to check if a given cell is valid cell or not
def isValid(x,y):
    if (x<R and y<C and x>=0 and y>=0):
        return True
    
    return False

# a function to mark all adjacent cells of landmines are unsafe

def markUnsafeCells(mat):
    for i in range(R):
        for j in range(C):
            # if a landmine is found 
            if mat[i][j]==0:
                # mark all adjacent cells
                for k in range(4):
                    if (isValid(i+rowNum[k],j+colNum[k])):
                        mat=[i+rowNum[k]][j+colNum[k]]=-1
    
    # mark all found adjacent cells as unsafe
    for i in range(R):
        for j in range(C):

            if mat[i][j]==-1:
                mat[i][j]=0


def findShortestPathUtil(mat,visited,i,j,dist):
    global min_dist
    # if destination is reached
    if (j==C-1):
        # update shortest path found so far
        min_dist=min(dist,min_dist)
        return
    
    # if current path cost exceeds minimum so far
    if (dist > min_dist):
        return 
    # include i,j in current path 
    visited[i][j]=True
    for k in range(4):
        if (isValid(i + rowNum[k], j + colNum[k]) and isSafe(mat, visited, i + rowNum[k], j + colNum[k])):
           findShortestPathUtil(mat, visited, i + rowNum[k], j + colNum[k], dist + 1)
    
    # backtrack 
    visited[i][j]=False 

# a wrapper function over
def findShortestPath(mat):
    global min_dist
    # stores minimum cost of shortest path so far
    min_dist = sys.maxsize
    # create a boolean matrix to store info about cells already visited in current route
    visited=[[False for i in range(C)] for j in range(R)]

    # mark adjacent cells of landmines as unsafe
    markUnsafeCells(mat)
    # start from first column and take minimum
    for i in range(R):
        # if path is safe from current cell
        if mat[i][0]==1:
            findShortestPathUtil(mat,visited,i,0,0)
            if min_dist==C-1:
                break