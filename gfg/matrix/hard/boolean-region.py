"""
Consider a matrix, where each cell contains either a '0' or a '1',
and any cell containing a 1 is called a filled cell. Two cells are said to be
connected if they are adjacent to each other horizontally, vertically, or diagonally.
If one or more filled cells are also connected, they form a region. find the size of the largest
region.

Approach:
Follow the given steps to solve the problem:

- A cell in the 2D matrix can be connected to at most 8 neighbors.
- So in DFS, make recursive calls for 8 neighbors of that cell.
  - keep a visited Hash-map to keep track of all visited cells.
  - Also, keep track of the visited 1's in every DFS and update the maximum
    size region.

"""
def isSafe(M,row,col,visited):
    global ROW,COL 

    return ((row>=0) and (row<ROW) and (col>=0) and (col < COL) and (M[row][col] and not visited[row][col]))

# A utility function to do DFS for a 2D boolean matrix. It only considers
# the 8 neighbours as adjacent vertices
# 

def DFS(M,row,col,visited,count):
    # These arrays are used to get row and column numbers of 8 neighbor of
    # a given cell
    rowNbr=[-1,-1,-1,0,0,1,1,1]
    colNbr=[-1,0,1,-1,1,-1,0,1]

    # mark this cell as visited
    visited[row][col]=True
    # recur for all connected neighbours
    for k in range(8):
        if (isSafe(M,row+rowNbr[k],col+colNbr[k],visited)):
            count+=1
            DFS(M,row+rowNbr[k],col+colNbr[k],visited,count)
            
