"""
Method 4: Using power of the matrix {{1,1},{1,0}} This is another
O(n) that relies on the fact that if we n times multiply the matrix
M={{1,1},{1,0}} to itself, in other words calculate power(M,n), then we
get the (n+1)th Fibonacci number as the element at row and column
(0,0) in the resultant matrix.

"""
def multiply(F,M):
    x=(F[0][0]*M[0][0]+F[0][1]*M[1][0])
    y = (F[0][0] * M[0][1] +
         F[0][1] * M[1][1])
    z = (F[1][0] * M[0][0] +
         F[1][1] * M[1][0])
    w = (F[1][0] * M[0][1] +
         F[1][1] * M[1][1])
     
    F[0][0] = x
    F[0][1] = y
    F[1][0] = z
    F[1][1] = w

def power(F, n):
 
    M = [[1, 1],
         [1, 0]]
 
    # n - 1 times multiply the
    # matrix to {{1,0},{0,1}}
    for i in range(2, n + 1):
        multiply(F, M)