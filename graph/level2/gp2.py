# program to count islands in boolean 2d matrix

class Graph:

    def __init__(self,row,col,g) -> None:
        self.ROW=row
        self.COL=col
        self.graph=g
    
    # a function to check if a given cell 
    # (row,col) can be included in DFS
    def isSafe(self,i,j,visited):
        return ( i>=0 and i < self.ROW and j>=0 self.COL and not visited[i][j] and self.graph[i][j] )
    
    # a utility function to do dfs for a 2d boolean
    # matrix. It only considers the 8 neighbour as adjacent vertices

    def DFS(self,i,j,visited):
        rowNbr=[-1,-1,-1,0,0,1,1,1]
        colNbr=[-1,0,1,-1,1,-1,0,1]
        visited[i][j]=True
        # recur for all connected neighbours
        for k in range(8):
            if self.isSafe(i+rowNbr[k],j+colNbr[k],visited):
                self.DFS(i+rowNbr[k],j+colNbr[k],visited)
            
    # the main function that returns count of islands
    # in a given boolean matrix
    def countIslands(self):
        visited=[[False for j in range(self.COL)] for i in range(self.ROW)]
        count=0
        for i in range(self.ROW):
            for j in range(self.COL):
                if visited[i][j]==False and self.graph[i][j]==1:
                    self.DFS(i,j,visited)
                    count+=1
        
        return count

class Graph:
    def __init__(self,row,col,graph) -> None:
        self.ROW=row
        self.COL=col
        self.graph=graph
    
    # a utility function to do dfs for a 2d
    # boolean matrix. it only considers the 8 neighbours
    # as adjacent vertices
    def DFS(self,i,j):
        if i<0 or i>= len(self.graph) or j<0 or j>= len(self.graph[0]) or self.graph[i][j]!=1:
            return
        # mark it is as visited
        self.graph[i][j]=-1
        #  recur for 8 neighbours
        self.DFS(i-1,j-1)
        self.DFS(i-1,j)
        self.DFS(i-1,j+1)
        self.DFS(i,j-1)
        self.DFS(i,j+1)
        self.DFS(i+1,j-1)
        self.DFS(i+1,j)
        self.DFS(i+1,j+1)
    
    def countIslands(self):
        count=0
        for i in range(self.ROW):
            for j in range(self.COL):
                if self.graph[i][j]==1:
                    self.DFS(i,j)
                    count+=1
        return count
