"""
We initialize the result as one of the two polynomials,
then we traverse the other polynomial and add all terms
to the result.

"""

def add(a,b,m,n):
    size=max(m,n)
    sum = [0 for i in range(size)]

    # initialize the product polynomial
    for i in range(0,m,1):
        sum[i]=a[i]
    
    # take over term of first polynomial
    for i in range(n):
        sum[i]+=b[i]
    
    return sum