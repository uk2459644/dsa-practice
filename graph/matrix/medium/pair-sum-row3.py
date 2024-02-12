"""
Method 3: Hashing
1. Create an empty hash table and store all elements of the matrix in the 
   hash as keys and their locations as values.

2. Traverse the matrix again to check for every element whether its pair exists
   in the hash table or not. If it exists, then compare row numbers.
"""
def pairSum(mat,n,sum):
    hm={}
    for i in range(n):
        for j in range(n):
            hm[(mat[i][j])]=[i,j]
    
    for i in range(n):
        for j in range(n):
            remSum=sum-mat[i][j]
            if remSum in hm:
                p=hm[remSum]
                row=p[0]
                col=p[1]

                if (row!=i and row > i):
                    print(mat[i][j],mat[row][col])
                    

