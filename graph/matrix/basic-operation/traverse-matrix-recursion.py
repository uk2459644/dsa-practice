"""
Given a matrix arr of size NxM, the task is to traverse this matrix using
recursion.

Approach: 
Check if the current position is in the bottom-right corner of the matrix
 - print the value at that position
 - end the recursion

"""
N=3
M=3

def traverse(arr,i,j):
    if i==N-1 and j==M-1:
        print(arr[i][j])
        return 
    
    print(arr[i][j], end=", ")
    if j<M-1:
        traverse(arr,i,j+1)
    elif i<N-1:
        traverse(arr,i+1,0)

