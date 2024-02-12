# A Naive recursive program to find length of the shortest supersequence

def superSeq(X,Y,m,n):
    if not m:
        return n
    
    if not n:
        return m
    
    if X[m-1]==Y[n-1]:
        return 1+superSeq(X,Y,m-1,n-1)
    
    return 1+min(superSeq(X,Y,m-1,n),superSeq(X,Y,m,n-1))



