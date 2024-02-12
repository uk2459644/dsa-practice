"""
Python implementation of Finding length of longest common
substring 

Returns length of longest common substring of X[0..m-1] and Y[0..n-1]

"""
def LCSubStr(X,Y,m,n):
    # Create a table to store length of longest common suffixes of substrings.
    
    # LCSuss is the table with zero value initially in each cell
    LCSuff=[[0 for k in range(n+1)] for l in range(m+1)]
    # to store the length of longest common substring
    result=0

    # Following steps to build LCSuff[m+1][n+1] in bottom up fashion
    for i in range(m+1):
        for j in range(n+1):
            if i==0 or j==0:
                LCSuff[i][j]=0
            elif X[i-1]==Y[j-1]:
                LCSuff[i][j]=LCSuff[i-1][j-1]+1
                result=max(result,LCSuff[i][j])
            else:
                LCSuff[i][j]=0

    return result



