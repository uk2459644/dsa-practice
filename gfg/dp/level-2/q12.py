
# Optimal strategy for a game usinng dp: 
# Follow the below steps to solve the problem: 
# - Create a 2-D array table of size N*N
# - Run a nested for loop to consider i and j at every possible position
#   with a distance equal to gap between them
"""
- Deaclare an  integer x, if i+2 is less than or equal to j then set x
  equal to table[i+2][j], else equal to zero.

- 
"""

def optimalStrategyOfGame(arr,n):
    # create a table to store solutions of subproblem
    table=[[0 for i in range(n)] for i in range(n)]
    # Fill table usinng recursive formula
    for gap in range(n):
        for j in range(gap,n):
            i=j-gap
            # here x is value of F(i+2,j),
            # y is F(i+1,j-1) and z is F(i,j-2) in above recursive formula
            x=0
            if (i+2)<=j:
                x=table[i+2][j]
            y=0
            if (i+1)<=(j-1):
                y=table[i+1][j-1]
            z=0
            if i<=(j-2):
                z=table[i][j-2]
            
            table[i][j]=max(arr[i]+min(x,y),arr[j]+min(y,z))
    return table[0][n-1]



