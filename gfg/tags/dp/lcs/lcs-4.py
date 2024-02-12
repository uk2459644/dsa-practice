"""
Dynamic programming implementation of LCS problem
Return length of LCS for X[0..m-1], Y[0..n-1]

"""
def lcs(X,Y,m,n):
    L=[[0 for i in range(n+1)] for j in range(m+1)]
    for i in range(m+1):
        for j in range(n+1):
            if i==0 or j==0:
                L[i][j]=0
            elif X[i-1]==Y[j-1]:
                L[i][j]=L[i-1][j-1]+1
            else:
                L[i][j]=max(L[i-1][j],L[i][j-1])
                

