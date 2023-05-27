"""
Method 2: Using BFS 

The idea is inspired from Lee algorithm and uses BFS.

1. We start from the source cell and call the BFS procedure.
2. We maintain a queue to store the coordinates of the matrix and
   initialize it with the source cell.
3. We also maintain a Boolean array visited of the same size as our 
  output matrix and initialize all its elements to false.

  1. We LOOP till queue is not empty
  2. Dequeue front cell from the queue
  3. Return if the destination coordinates have been reached.
  4. For each of its four adjacent cells, if the value is 1 and
     they are not visited yet, we enqueue it in the queue and also mark
     them as visited.

"""
from collections import deque

ROW=9
COL=10

class Point:
    def __init__(self,x:int,y:int) -> None:
        self.x=x
        self.y=y

# A data structure for queue used in BFS
class queueNode:
    def __init__(self,pt:Point,dist:int) -> None:
         self.pt=pt
         self.dist=dist

# check whether given cell is a valid or not
def isValid(row:int,col:int):
    return (row>=0) and (row<ROW) and (col>=0) and (col<COL)

# These arrays are used to get row and column numbers of 4 neighbours of
# a given cell

rowNum = [-1,0,0,1]
colNum = [0,-1,1,0]

# Function to find the shortest path between a given source cell to
# a destination cell

def BFS(mat,src:Point,dest:Point):
    # checck source and destination cell of the matrix have value 1
    if mat[src.x][src.y]!=1 or mat[dest.x][dest.y]!=1:
        return -1
    
    visited=[[False for i in range(COL)] for j in range(ROW) ]
    # mark the source cell as visited
    visited[src.x][src.y]=True
    # create a queue for BFS 
    q=deque()
    # Distance of source cell is 0
    s=queueNode(src,0)
    q.append(s)

    # Do a BFS starting from source cell
    while q:
        curr=q.popleft()
        # if we have reached the destination cell, we are done
        pt=curr.pt

        if pt.x == dest.x and pt.y==dest.y:
            return curr.dist
        
        # Otherwise enqueue its adjacent cells
        for i in range(4):
            row=pt.x+rowNum[i]
            col=pt.y+colNum[i]
            # if adjacent cell is valid, has path and not visited yet,
            # enqueue it
            if (isValid(row,col) and mat[row][col]==1 and not visited[row][col]):
                visited[row][col]=True
                Adjcell = queueNode(Point(row,col),curr.dist+1)
                q.append(Adjcell)
    
    return -1



