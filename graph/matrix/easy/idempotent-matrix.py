"""
Idempotent matrix: 

A matrix is said to be idempotent matrix if matrix multiplied by
itself return the same matrix. The matrix M is said to be idempotent
matrix if and only if M*M=M.
"""
import math

def multiply(mat,res):
    N=len(mat)

    for i in range(0,N):
        for j in range(0,N):
            res[i][j]=0
            for k in range(0,N):
                res[i][j]+=mat[i][k]*mat[k][j]

def checkIdempotent(mat):
    N=len(mat)
    # calculate multiplication of matrix
    # with itself and store it into res.
    res=[[0]*N for i in range(0,N)]

    multiply(mat,res)
    for i in range(0,N):
        for j in range(0,N):
            if (mat[i][j]!=res[i][j]):
                return False
    
    return True
