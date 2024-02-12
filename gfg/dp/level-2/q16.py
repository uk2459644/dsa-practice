
def superSeq(X,Y,n,m,lookup):
    if m==0 or n==0:
        lookup[n][m]=n+m
    
    if lookup[n][m]==0:
        if X[n-1]==Y[m-1]:
            lookup[n][m]=superSeq(X,Y,n-1,m-1,lookup)+1
        else:
            lookup[n][m]=min(superSeq(X,Y,n-1,m,lookup)+1,superSeq(X,Y,n,m-1,lookup)+1)
    
    return lookup[n][m]

