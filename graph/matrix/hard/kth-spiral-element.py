"""
Given a 2D Matrix of order nXm, print K'th element in the spiral
 form of the matrix. See the following.

 Simple Approach: One simple solution is to start traversing matrix in spiral
 form and start a counter. Whenever count gets equal to k, print that element.


"""

R=3
C=6

def spiralPrint(m,n,a,c):
    k=0
    l=0
    count=0
    """
    k-starting row index
    m-ending row index
    l-starting column index
    n-ending column index
    i-iterator
    """
    while (k<m and l<n):
        for i in range(l,n):
            count+=1
            if (count==c):
                print(a[k][i])
        
        k+=1
        # check the last column from the remaining columns
        for i in range(k,m):
            count+=1
            if (count==c):
                print(a[i][n-1])
        n-=1
        # check the last row from the remaining rows
        if k<m:
            for i in range(n-1,l-1,-1):
                count+=1
                if count == c:
                    print(a[m-1][i])
                m-=1
        # check the first column from the remaining columns
        if l<n:
            for i in range(m-1,k-1,-1):
                count+=1
                if count == c:
                    print(a[i][l])
            
            l+=1
            
