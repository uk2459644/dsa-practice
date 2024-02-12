"""
Diagonal Matrix: 
A square matrix is said to be a diagonal matrix if the elements
of the matrix except the main diagonal are zero. A square null 
matrix is also a diagonal matrix whose main diagonal elements are 
zero.
"""
def isDiagonalMatrix(mat,N):
    for i in range(0,N):
        for j in range(0,N):
            # condition to check other elements except 
            # main diagonal are zero or not.
            if ((i!=j) and (mat[i][j]!=0)):
                return False
    
    return True

"""
Scalar Matrix: 
A square matrix is said to be a scalar matrix if all the main diagonal
elements are equal and other elements except main diagonal are zero.
The scalar matrix can also be written in form of n*I, where n is any
real number and I is the identity matrix.
"""
def isScalarMatrix(mat,N):
    # check all elements except main diagonal are zero or not.

    for i in range(0,N):
        for j in range(0,N):
            if ((i!=j) and (mat[i][j]!=0)):
                return False
    
    # Check all diagonal elements are same or not.
    for i in range(0,N-1):
        if (mat[i][i]!=mat[i+1][i+1]):
            return False
    
    return True
