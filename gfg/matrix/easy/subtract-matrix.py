"""
Subtract Matrix:

"""

N=4

def subtract(A,B,C):
    for i in range(N):
        for j in range(N):
            C[i][j]=A[i][j]-B[i][j]
            