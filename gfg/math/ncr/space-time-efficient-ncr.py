"""
Change r to n-r if r is greater than n-r, and create a variable to store
the answer.

Run a loop from 0 to r-1

C(n,k)=C(n,n-k)

"""
def binomialCoefficient(n,k):
    if k>n-k:
        k=n-k
    
    res=1

    for i in range(k):
        res=res*(n-i)
        res=res//(i+1)
    
    return res

