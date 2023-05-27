"""
Given an nxn square matrix, find sum of all sub-square matrix.

Simple Solution:
is to one by one pick starting point (leftmost-topmost corner) of all 
possible sub-squares. Once the starting point is picked, calculate sum of 
sub-square starting with the picked starting point.

"""
n=5

def printSumSimple(mat,k):
    # k must be smaller than or equal to n
    if k>n:
        return 
    
    # row number of first cell in current
    # sub-square of size kxk

    for i in range(n-k+1):
        # column of first cell in current sub-square of size kxk
        for j in range(n-k+1):
            # Calculate and print sum of current sub-square
            sum=0
            for p in range(i,k+i):
                for q in range(j,k+j):
                    sum+=mat[p][q]
            
            print(sum)
            
