"""
Given a square matrix, turn it by 90 degrees in anti-clockwise direction 
without using any extra space.

Approach: The idea is to find the transpoes of the matrix and then
reverse the column of the transposed matrix.

A transpose of a matrix is when the matrix is flipped over its diagonal
the row index of an element becomes the column index and vice versa.
"""
R=4
C=4

def reverseColumn(arr):
    for i in range(C):
        j=0
        k=C-1
        while j<k:
            t=arr[j][i]
            arr[j][i]=arr[k][i]
            arr[k][i]=t
            j+=1
            k-=1

# function for do transpose of matrix
def transpose(arr):
    for i in range(R):
        for j in range(i,C):
            t=arr[i][j]
            arr[i][j]=arr[j][i]
            arr[j][i]=t
            

