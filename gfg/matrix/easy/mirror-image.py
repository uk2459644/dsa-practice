"""
Given a 2-D array of order NxN, print a matrix that is the mirror
of the given tree across the diagonal. We need to print the result
in a way: swap the values of the triangle above the diagonal with the
values of the triangle below it like a mirror image swap.
"""
MAX=100

def imageSwap(mat,n):
    # for diagonal which start from at first row of matrix
    row=0
    # traverse all top right diagonal
    for j in range(n):
        # here we use stack for reversing the element of diagonal
        s=[]
        i=row
        k=j
        while (i<n and k>=0):
            s.append(mat[i][k])
            i+=1 
            k-=1 
            s.pop()
        
        # do the same process for all the diagonal which start from 
        # last column
        column=n-1
        for j in range(1,n):
            s=[]
            i=j
            k=column
            

