"""
Initially, there is a grid with some cells which may be alive or dead.
Our task is to generate the next generation of cells based on the following
rules:

1. Any live cell with fewer than two live neighbors fies as if caused by
   underpopulation.

2. Any live cell with two or three live neighbors lives on to the 
   next generation.

3. Any live cell with more than three live neighnors dies, as if by 
   overpopulation.

4. Any dead cell with exactly three live neighbors becomes a live cell, as
 if by reproduction.
 
"""
def nextGeneration(grid,M,N):
   future=[[0 for i in range(N)] for j in range(M)]
   #  loop through every cell
   for l in range(M):
      for m in range(N):
         # finding no of neighbours that are alive
         aliveNeighbours=0
         for i in range(-1,2):
            for j in range(-1,2):
               if ((l+i>=0 and l+i<M) and (m+j>=0 and m+j <N)):
                  aliveNeighbours+=grid[l+i][m+j]
         
         # The cell needs to be subtracted from its neighbours as it
         # was counted beore
         aliveNeighbours-=grid[l][m]
         # Implementing the Rules of life
         # cell is lonely and dies
         if ((grid[l][m]==1) and (aliveNeighbours<2)):
            future[l][m]=0
         # cell dies due to over population
         elif ((grid[l][m]==1) and (aliveNeighbours>3)):
            future[l][m]=0
         # a new cell is born
         elif ((grid[l][m]==0) and (aliveNeighbours==3)):
            future[l][m]=1
         # remains the same
         else:
            future[l][m]=grid[l][m]
            

    
    
