# Minimum number of deletion and insertion to transform one string into another

"""
Efficient Approach: 
Algorithm:

- str1 and str2 be the given strings
- m and n be their lengths respectively.
- len be the length of the longest common subsequence of str1 and str2
- minimum number of deletion minDel=m-len
- minimum number of insertion minInsert=n-len

"""
def lcs(str1,str2,m,n):
    L=[[0 for i in range(n+1)] for i in range(m+1)]
    
    # Following steps build L[m+1][n+1]
    # in bottom up fashion. Note that L[i][j] contains length of LCS
    # of str1[0..i-1] and str2[0..j-1]

    for i in range(m+1):
        for j in range(n+1):
            if (i==0 or j==0):
                L[i][j]=0
            elif (str1[i-1]==str2[j-1]):
                L[i][j]=L[i-1][j-1]+1
            else:
                L[i][j]=max(L[i-1][j],L[i][j-1])
    
    return L[m][n]



