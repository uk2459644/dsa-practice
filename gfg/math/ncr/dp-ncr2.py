"""
Python program to find the nCr%p based on optimal dynamic
programing implementation and Pascal Triangle concepts.

"""

def moduloMultiplication(a,b,mod):
    res=0
    # update a if it is more than or equal to mod
    a%=mod

    while b:
        # if b is odd, add a with result
        if (b&1):
            res=(res+a)%mod
        # here we assume that doing 2*a doesn't cause overflow
        a=(2*a)%mod
        b>>=1
    
    return res

x,y=0,1

def gcdExtended(a,b):
    global x,y 
    if (a==0):
        x=0
        y=1
        return b
    
    gcd=gcdExtended(b%a,a)
    x1=x
    y1=y
    # update x and y using results of recursive call
    x=y1-int(b/a)*x1
    y=x1

    return gcd

def modInverse(a,m):
    g=gcdExtended(a,m)
    # return -1 if b and m are not co-prime
    if g!=1:
        return -1
    
    return (x%m+m)%m

# function to compute a/b under modulo m
def modDivide(a,b,m):
    a=a%m
    inv=modInverse(b,m)

    if (inv==-1):
        return 0
    else:
        return (inv*a)%m
    
# function to calculate nCr%p 

def nCr(n,r,p):
    # edge case which is not possible
    if r>n:
        return 0
    
    if r>n-r:
        r=n-r
    
    x=1

    for i in range(1,r+1):
        x=moduloMultiplication(x,(n+1-i),p)

        x=modDivide(x,i,p)
    
    return x


