"""
Matrix Chain Multiplication

Given the dimension of a sequence of matrices in an array arr[], where 
the dimension of the ith matrix is (arr[i-1]*arr[i]), the task is to find
the most efficient way to multiply these matrices together such that the 
total number of element multiplication is minimum.

Matrix Chain Multiplication using Recursion:

Facts: 

Two matrices of size m*n and n*p when multiplied, they generate a matrix
of size m*p and the number of multiplication performed are m*n*p.

Now, for a given chain of N matrices, the first partition can be done in
N-1 ways. For example, sequence of matrices A,B,C and D can be grouped as
(A)(BCD), (AB)(CD) or (ABC)(D) in these three ways.

Approach: 
- Create a recursive function that takes i and j as parameters that determines
  the range of a group.
  - Iterate from k=i to j to partition the given range into two groups.
  - Call the recursive function for these groups.
  - Return the minimum value among all the partion as the required minimum
    number of multiplication to multiply all the matrices of this group.
- The minimum value returned for the range 0 to N-1 is the required answer.

"""
import sys

def matrixChainOrder(p,i,j):
    if i==j:
        return 0
    
    _min=sys.maxsize
    # place parenthesis at different places between first and last matrix,
    # recursively calculate count of multiplications for each parenthesis
    # placement and return the minimum count

    for k in range(i,j):
        count=(matrixChainOrder(p,i,k)+matrixChainOrder(p,k+1,j)+p[i-1]*p[k]*p[j])

        if count < _min:
            _min=count
    
    return _min

