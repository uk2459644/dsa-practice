"""
A simple solution is to one by one consider every term of the
first polynomial and multiply it with every term of the 
second polynomial.
"""

def multiply(a,b,m,n):
    prod=[0]*(m+n-1)

    for i in range(m):
        for j in range(n):
            prod[i+j]+=a[i]*b[j]
    
    return prod

