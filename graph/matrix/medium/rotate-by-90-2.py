"""
Another Approach using a single traversal of the matrix:

The idea is to traverse along the boundaries of the matrix and
shift the position of the elements in 90 anticlockwise directions in
each boundary. There are such (n/2-1) boundaries in the matrix.

Algorithm: 
1.Iterate over all the boundaries in the matrix. There are total (n/2-1)
 boundaries.

2. For each boundary take the 4 corner elements and swap them such that the
4 corner elements get rotated in anticlockwise directions. then take 
next 4 elements along the edges(left,right,top, bottom) and swap them
in an anticlockwise direction. Continue as long as all the elements in that
particular boundary get rotated in 90 degree anticlockwise directions.

3. Then move on to the next innner boundary and continue the process as
long the whole matrix is rotated in 90 degree anticlockwise direction.
"""
def rotate90(arr):
    n=len(arr)
    a,b,c,d=0,0,0,0

    for i in range(n//2):
        for j in range(n-2*i-1):
            a=arr[i+j][i]
            b=arr[n-1-i][i+j]
            c=arr[n-1-i-j][n-1-i]
            d=arr[i][n-1-i-j]

            arr[i+j][i]=d
            arr[n-1-i][i+j]=a
            arr[n-1-i-j][n-1-i]=b
            arr[i][n-1-i-j]=c
            
