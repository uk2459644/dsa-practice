"""
We are given an m*n matrix of positive integers and a row
number. The task is to find all rows in given matrix which are permutations
of given row elements. It is also given that values in every row are distinct.
"""
"""
A simple solution is to one by one sort all rows and check all rows. 
If any row is completely equal to the given row, that means the current row is
is a permutation of the given row.
"""
"""
An efficient approach is to use hashing. Simply create a hash_set for the 
given row. After hash set creation, traverse through the remaining rows, and for every
row check if all of its elements are present in the hash set or not.
"""

def permutatedRows(mat,m,n,r):
    s=set()

    for j in range(n):
        s.add(mat[r][j])
    
    for i in range(m):
        if i==r:
            continue

        for j in range(n):
            if mat[i][j] not in s:
                j=j-2
        
        if j+1!=n:
            continue

        print(i)
