"""
Rotate a Matrix by 180 degree

Given a square matrix, the task is that turn it by 180 degrees 
in an anti-clockwise direction without using any
extra space.

There are four steps that are required to solve this
problem: 
1- find the transpose of a matrix.
2- reverse columns of the transpose
3- find the transpose of a matrix
4- reverse columns of the transpose

"""
R=4
C=4

def reverseColumns(arr):
    for i in range(C):
        for j in range(0,int(C/2)):
            x=arr[j][i]
            arr[j][i]=arr[C-1-j][i]
            arr[C-1-j][i]=x

def transpose(arr):
    for i in range(R):
        for j in range(i,C):
            x=arr[j][i]
            arr[j][i]=arr[i][j]
            arr[i][j]=x
    

