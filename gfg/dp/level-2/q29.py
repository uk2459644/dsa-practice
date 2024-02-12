# Dynamic Programming solution for matrix chain multiplication using
# Tabulation:

"""
In iterative approach, we initially need to find the number of multiplications
required to multiply two adjacent matrices. We can use these values to find
the minimum multiplication required for matrices in a range of length 3 and
further use those values for ranges with higher length.

"""
import sys
maxint=int(1e9+7)

# matrix ai has dimension p[i-1]xp[i]

def MatrixChainOrder(p,n):
    # for simplicity of the program one extra row and column are allocated
    # in m[][]. 0th row and 0th column of m[][] are not used
    m=[[0 for x in range(n)] for x in range(n)]

    # m[i,j]=Minimum number of scalar multiplications needed to compute
    # the matrix A[i]A[i+1]...A[j]=A[i..j] where dimension of A[i] is p[i-1]xp[i]

    # cost is zero when multiplying one matrix
    for i in range(1,n):
        m[i][i]=0
    
    # L is chain length
    for L in range(2,n):
        for i in range(1,n-L+1):
            j=i+L-1
            m[i][j]=maxint
            for k in range(i,j):
                # q=cost / scalar multiplications
                q=m[i][k]+m[k+1][j]+p[i-1]*p[k]*p[j]
                if q<m[i][j]:
                    m[i][j]=q
                    

