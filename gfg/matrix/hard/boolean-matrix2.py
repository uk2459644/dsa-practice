"""
Another approach:

Follow the steps below to solve the problem

- Create two temporary array row[M] and col[N]. Initialize all values of row[]
  and col[N]. Initialize all values of row[] and col[] as 0.

- Traverse the input matrix mat[M][N]. If you see an entry mat[i][j] as true,
  then mark row[i] and col[j] as true.
"""
R=3
C=4

def modifyMatrix(mat):
    row=[0]*R
    col=[0]*C

    # Initialize all values of row[] as 0
    for i in range(0,R):
        row[i]=0
    
    # Initialize all values of col[] as 0
    for i in range(0,C):
        col[i]=0
    # store the rows and columns to be marked as 1 in row[] and col[] 
    # arrays respectively
    for i in range(0,R):
        for j in range(0,C):
            if (mat[i][j]==1):
                row[i]=1
                col[j]=1
    
    for i in range(0,R):
        for j in range(0,C):
            if (row[i]==1 or col[j]==1):
                mat[i][j]=1
                
