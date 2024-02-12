"""
Dynamic Programming Solution for Matrix Chain Multiplication using
Tabulation (Iterative Approach):

In iterative approach, we initially need to find the number of multiplication
required to multiply two adjacent matrices. We can use these values to find
the minimum multiplication required for matrices in a range of length with higher
lengths.

Build on the answer in this manner till the range becomes [0,n-1].

"""
"""
Approach: 

- Iterate from l=2 to n-1 which denotes the length of the range:
  - Iterate from i=0 to n-1:
    - Find the right end of the range (j) having l matrices.
    - iterate from k=i+1 to j which denotes the point of partition.
      - multiply the matrices in range (i,k) and (k,j).
      - This will create two matrices with dimensions arr[i-1]*arr[k]
        and arr[k]*arr[j].
      - The number of multiplications to be performed to multiply these
        two matrices say X are arr[i-1]*arr[k]*arr[j].
      - The total number of multiplications is dp[i][k]+dp[k+1][j]+X.

-The value stored at dp[1][n-1] is the required answer.
"""
import sys
maxint=int(1e9+7)

def matrixChainOrder(p,n):
    # for simplicity of the program, one extra row and one extra column are
    # allocated in m[][].
    # 0th row and 0th column of m[][] are not used.
    m=[[0 for x in range(n)] for x in range(n)]
    for i in range(1,n):
        m[i][i]=0

    for l in range(2,n):
        for i in range(1,n-l+1):
            j=i+l-1
            m[i][j]=maxint
            