"""
Given a matrix of distinct values and a sum. The task is to find all the 
pairs in a given matrix whose summation is equal to the given sum. 

Each element of a pair must be from different rows, the pair must not
lie in the same row.

Method 1:
A simple solution for this problem is to, one by one. Take each element 
of all rows and find pairs starting from the next immediate row in the matrix.


"""

def pair_sum(mat,sum):
    count=0
    m=len(mat)
    n=len(mat[0])

    for i in range(m):
        for j in range(i+1,m):
            for k in range(n):
                for l in range(n):
                    if mat[i][k]+mat[j][l]==sum:
                        count+=1
                        print(mat[i][k],mat[j][l])
    
    return count

