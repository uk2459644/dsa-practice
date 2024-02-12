"""
Number of islands using DFS:
The idea is to modify the given matrix, and perform DFS to find the total
number of islands.

Follow the steps below to solve the problem:

- Initialize count=0, to store the answer.
- Traverse a loop from 0 till ROW
  - Traverse a nested loop from 0 to COL
    - If the value of the current cell in the given matrix is 1
      - increment count by 1
      - Call DFS function
        - If the cell exceeds the boundary or the value at the current cell is 0
          - return
        - update the value at the current cell as 0.
        call DFS on the neighbour recursively

- Return count as the final answer.
"""
class Graph:
    def __init__(self,row,col,graph) -> None:
        self.ROW=row
        self.COL=col
        self.graph=graph
    
    # a utility function to do DFS for a 2D 
    # boolean matrix. It only considers the 8 neighbours as adjacent vertices
    def DFS(self,i,j):
        if i<0 or i>=len(self.graph) or j<0 or j>=len(self.graph[0]) or self.graph[i][j]!=1:
            return
        # mark it as visited
        self.graph[i][j]=-1
        # recur for 8 neighbours
        self.DFS(i-1,j-1)
        self.DFS(i-1,j)
        self.DFS(i-1,j+1)
        self.DFS(i,j-1)
        self.DFS(i,j+1)
        self.DFS(i+1,j-1)
        self.DFS(i+1,j)
        self.DFS(i+1,j+1)
    
    # The main function that returns count of islands in a given boolean 2D matrix
    def countIslands(self):
        # Initialize count as 0 and traverse through the all cells of given matrix
        count=0
        for i in range(self.ROW):
            for j in range(self.COL):
                # If a cell with value 1 is not visited yet then new island found
                if self.graph[i][j]==1:

                    # visit all cells in this island and increment island counnt
                    self.DFS(i,j)
                    count+=1 
        
        return count
    
