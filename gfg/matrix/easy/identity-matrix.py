"""
Identity Matrix: 
The dictionary definition of an Identity Matrix is a square 
matrix in which all the elements of the principal or main
diagonal are 1's and all other elements are zeros.

A property of the identity matrix is that it leaves a matrix unchanged
if it is multiplied by an identity matrix.
"""
def Identity(size):
    for row in range(0,size):
        for col in range(0,size):
            if (row==col):
                print("1")
            else:
                print("0")

def isIdentity(mat,N):
    for row in range(N):
        for col in range(N):
            if (row==col and mat[row][col]!=1):
                return False
            elif (row!=col and mat[row][col]!=0):
                return False
    
    return True
