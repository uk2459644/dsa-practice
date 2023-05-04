"""
Sorting matrix: 

Given a nXn matrix. The problem is to sort the given matrix
in strict order. Here strict order means that the matrix is sorted
in a way such that all elements in a row are sorted in increasing order
and for row 'i', where 1<=i<=n-1, the first element of row 'i' is greater
than or equal to the last element of row 'i-1'.
"""
def sortMat(mat,n):
    temp=[0]*n*n
    k=0

    for i in range(0,n):
        for j in range(0,n):
            temp[k]=mat[i][j]
            k+=1 
    
    temp.sort(reverse=True)
    k=0
    for i in range(0,n):
        for j in range(0,n):
            mat[i][j]=temp[k]
            
