"""
Efficient Approach: 

While traversinng the array in spiral order, a loop is used to traverse the
sides. So if it can be found out that the kth element is in the given side then
the kth element can be found out in constant time. This can be done recursively
as well as iteratively.

Algorithm:

"""
MAX=100

# function for kth element

def findK(A,n,m,k):

    if (n<1 or m<1):
        return -1
    
    # if element is in outermost ring

    # element is in first row
    if k <= m:
        return A[0][k-1]
    
    # element is in last column
    if (k<=(m+n-1)):
        return A[(k-m)][m-1]
             
    ''' Element is in last row '''
    if (k <= (m + n - 1 + m - 1)):
        return A[n - 1][m - 1 - (k - (m + n - 1))]
     
    ''' Element is in first column '''
    if (k <= (m + n - 1 + m - 1 + n - 2)):
        return A[n - 1 - (k - (m + n - 1 + m - 1))][0]
         
         
    '''....If element is NOT in outermost ring ....'''
    ''' Recursion for sub-matrix. &A[1][1] is
    address to next inside sub matrix.'''
    A.pop(0)
    [j.pop(0) for j in A]
    return findK(A, n - 2, m - 2, k - (2 * n + 2 * m - 4))
 
    
