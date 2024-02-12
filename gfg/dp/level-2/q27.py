# Given the dimension of a sequence of matrices in an array arr[],
# where the dimension of the ith matrix is (arr[i-1]*arr[i]), the task is
# to find the most efficient way to multiply these matrices together such
# that the total number of element multiplication is minimum.

"""
Approach : 

Two matrices of size m*n and n*p when multiplied, they generate a matrix
of size m*p and the number of multiplications performed are m*n*p.

Now, for a given chain of N matrices, the first partition can be done 
in N-1 ways.

So a range [i,j] can be broken into two groups like {[i,i+1],[i+1,j]},
{[i,i+2],[i+2,j]},...,{[i,j-1],[j-1,j]}.

- Each of the group can be further partioned into smaller groups and we can
  find the total required multiplications by solving for each of the groups.

- The minimum number of multiplications among all the first partitions is
  the required answer.

"""
"""
Follow the steps mentioned below to implement the approach: 

- Create a recursive function that takes i and j as parameters that determines
  the range of a group.
  - Iterate from k=i to j to partition the given range into two groups.
  - Call the recursive function for these groups.
  - Return the minimum value among all the partitions as the required minimum
    number of multiplications to multiply all the matrices of this group.
- The minimum value returned for the range 0 to N-1 is the required answer.

"""
# Python code to implement the matrix chain multiplication using recursion

import sys
# Matrix A[i] has dimension p[i-1]xp[i]
# for i=i..n

def MatrixChainOrder(p,i,j):
    if i==j:
        return 0
    
    _min=sys.maxsize
    # Place parenthesis at different places between first and last matrix,
    # recursively calculate counnt of multiplications for each parenthesis
    # placement and return the minimum count
    for k in range(i,j):
        count=(MatrixChainOrder(p,i,k)+MatrixChainOrder(p,k+1,j)+p[i-1]*p[k]*p[j])

        if count < _min:
            _min=count

    # return minimum counnt
    return _min



