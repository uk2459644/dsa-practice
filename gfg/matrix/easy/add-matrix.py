"""
Given two NxM matrices. Find a NxM matrix as the sum of given matrices each
value at the sum of values of corresponding elements of the given two matrices.

Approach: Below is the idea to solve the problem.

Iterate over every cell of matrix (i,j), add the corresponding values of the  
and store in a single matrix, the resultant matrix.

"""
N=4

def add(A,B,C):
    for i in range(N):
        for j in range(N):
            C[i][j]=A[i][j]+B[i][j]
            

