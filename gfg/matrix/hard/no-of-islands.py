"""
No Of Islands.

The idea is to keep an additional matrix to keep trck of the visited nodes in the
given matrix, and perform DFS to find the total number of islands.

Follow the steps below to solve the problem:
- Initialize a boolean matrix visited of the size of the given
  matrix to false.
- Initialize count=0, to store the answer.
- Traverse a loop from 0 to ROW
  - Traverse a nested loop from 0 to COL
    - If the value of the current cell in the given matrix is 1 and is not visited
      - Call DFS function
        - Initialize rowNbr[]={-1,-1,-1,0,0,1,1,1} and colNbr[]={-1,0,1,-1,1,-1,0,1}
           for the neighbour cells.
        - Mark the current cell as visited
        - Run a loop from 0 till 8 to traverse the neighbor
          - If the neighbour is safe to visit and is not visited
            - call DFS recursively on the neighbour
- return count as the final answer
"""

class Graph:
    def __init__(self,row,col,g) -> None:
        self.ROW=row
        self.COL=col
        self.graph=g
    
    # A function to check is a given cell (row, col) can be included in DFS
    def isSafe(self,i,j,visited):
        # row number is in range, column number is in range and value is 1
        # and not yet visited
        return (i>=0 and i<self.ROW and j>=0 and j<self.COL and not visited[i][j] and self.graph[i][j])
    
    # A utility function to do DFS for a 2D boolean matrix. It only considers the 8
    # neighbours as adjacent vertices
    def DFS(self,i,j,visited):
        # These arrays are used to get row and column numbers of 8 neighbours
        # of a given cell
        rowNbr=[-1,-1,-1,0,0,1,1,1]
        colNbr=[-1,0,1,-1,1,-1,0,1]
        # mark this cell as visited
        visited[i][j]=True
        # recur for all connected neighbours
        for k in range(8):
            if self.isSafe(i+rowNbr[k],j+colNbr[k],visited):
                self.DFS(i+rowNbr[k],j+colNbr[k],visited)
    
    # The main function that returns count of islands in a given booolean 2D matrix
    def countIslands(self):
        # make a bool array to mark visited cells.
        # initially all cells are unvisited.
        visited=[[False for j in range(self.COL)] for i in range(self.ROW)]
        # Initialize count as 0 and traverse through the all cells of the matrix
        count=0
        for i in range(self.ROW):
            for j in range(self.COL):
                # if a cell with value 1 is not visited yet, then new island found
                if visited[i][j]==False and self.graph[i][j]==1:
                    # visite all cells in this island and increment island count
                    self.DFS(i,j,visited)
                    count+=1 
        
        return count
    
