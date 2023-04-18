
class Graph:
    def __init__(self,row,col,g) -> None:
        self.ROW = row
        self.COL = col
        self.graph = g
    
    def isSafe(self,i,j,visited):
        # row number is in range, column number is in range
        # and value is 1 and not visited

        return (i>=0 and i< self.ROW and j>=0 and j<self.COL
                and not visited[i][j] and self.graph[i][j])
    
    def DFS(self,i,j,visited):
        # these arrays are used to get row and column
        # numbers of 8 neighbours of a given cell
        rowNbr = [-1,-1,-1,0,0,1,1,1]
        colNbr = [-1,0,1,-1,1,-1,0,1]
        # mark this cell as visited
        visited[i][j]=True
        # Recur for all connected neighbours 
        for k in range(8):
            if self.isSafe(i+rowNbr[k],j+colNbr[k],visited):
                self.DFS(i+rowNbr[k], j+colNbr[k],visited)
    
    def countIslands(self):
        # mark a bool array to mark visited cells.
        # initially all cells are unvisited
        visited=[[False for j in range(self.COL)] for i in range(self.ROW)]

        # initialize count as 0 and traverse through the all cells of given matrix

        count=0
        for i in range(self.ROW):
            for j in range(self.COL):
                # if a cell with vlue 1 is not visited yet,
                # then new island found
                if visited[i][j] == False and self.graph[i][j]==1:
                    self.DFS(i,j,visited)
                    count+=1
        return count

graph = [[1,1,0,0,0],
         [0,1,0,0,1],
         [1,0,0,1,1],
         [0,0,0,0,0,0],
         [1,0,1,0,1]]

row=len(graph)
col=len(graph[0])

g= Graph(row,col,graph)

print("Number of islands is:")
print(g.countIslands())



