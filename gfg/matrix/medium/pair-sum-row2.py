"""
Given a matrix of distinct values and a sum. The task is to find all
the pairs in a given matrix whose summation is equal to the given sum.
Each element of a pair must be from different row.
"""
"""
Method 1: 
A simple solution for this problem is to, one by one, take each element of all
rows and find pairs starting from the next immediate row in the matrix.

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
                        print("yes")


"""
Method 2:
Using Sorting
- Sort all the rows in ascending order. The time complexity for this 
  preprocessing will be O(n^2logn).

  - Now we will select each row one by one and find pair elements in the 
    remaining rows after the current row.

 - Take two iterators, left and right. left iterator points left corner of
   the current i'th row and right iterator points right corner of the next
   j'th row in which we are going to find a pair of elements.

 - If mat[i][left]+mat[j][right] <  sum then left++ i.e, move in i'th row
   towards right corner, otherwise right++ i.e., move in j'th row towards
   the left corner.
"""

MAX=100

def pairSum(mat,n,sum):
    for i in range(n):
        mat[i].sort()
    
    for i in range(n-1):
        for j in range(i+1,n):
            left=0
            right=n-1
            while (left<n and right>=0):
                if ((mat[i][left]+mat[j][right])==sum):
                    print("(",mat[i][left],mat[j][right],")")
                    left+=1
                    right-=1
                else:
                    if ((mat[i][left]+mat[j][right])<sum):
                        left+=1
                    else:
                        right-=1 
                        

    
