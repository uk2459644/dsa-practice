# Dynamic programming implementation of LCS problem

def lcs(X,Y,m,n):
    # Declaring the array for storing the dp value
    L=[[None]*(n+1)]*(m+1)

    # Following steps build L[m+1][n+1] in bottom up fashion
    for i in range(m+1):
        for j in range(n+1):
            if i==0 or j==0:
                L[i][j]=0
            elif X[i-1]==Y[j-1]:
                L[i][j]=L[i-1][j-1]
            else:
                L[i][j]=max(L[i-1][j],L[i][j-1])
    
    return L[m][n]



