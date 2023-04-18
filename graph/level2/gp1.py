# Program to find islands in boolean 2d

class Graph:
    def __init__(self,row,col,g) -> None:
        self.ROW=row 
        self.COL=col
        self.graph=g
    
    # a function to check if a given cell
    #(row,col) can be included in DFS
    def isSafe(self,i,j,visited):
        # row number is in range, column number is 
        # in range and value is 1 and not yet visited
        return (i>=0 and i<self.ROW and j>=0 and j<self.COL
                and not visited[i][j] and self.graph[i][j])
    
    # a utility function to do DFS for a 2d boolean
    # matrix. It only considers the 8 neighbours as adjacent
    # vertices
    def DFS(self,i,j,visited):
        # these arrays are used to get row and column
        # number of 8 neighbours 
        # of given cell
        rowNbr = [-1,-1,-1,0,0,1,1,1]
        colNbr = [-1,0,1,-1,1,-1,0,1]
        # mark this cell as visited
        visited[i][j]=True
        
