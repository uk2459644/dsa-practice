"""
METHOD 1: Using Dynamic Programming:

A Simple solution is to first compute nCr, then compute nCr%p. this 
solution works fine when the value of nCr is small.

What if the value of nCr is large?
The value of nCr%p is generally needed for large values of n,
when nCr cannot fit in a variable, and causes overflow. So computing
nCr and then using modular operator is not a good idea as there will be overflow
even for slightly larger value of n and r.

The idea is to compute nCr using below formula

C(n,r)=C(n-1,r-1)+C(n-1,r)
C(n,0)=C(n,n)=1

Extension of above formula for modular arithmetic:
We can use distributive property of modular operator to find nCr%p
using above formula.

C(n,r)%p=[C(n-1,r-1)%p + C(n-1,r)%p]%p 
C(n,0)=C(n,n)=1
"""
def ncrModp(n,r,p):
    # optimization for the cases when r is large compared to n-r
    if (r>n-r):
        r=n-r
    
    # The array C is going to store last row of pascal triangle
    # at the end. And last entry of last row is nCr.
    C=[0 for i in range(r+1)]
    C[0]=1
    # one by  one constructs remaining rows of pascal triangle from
    # top to bottom
    for i in range(1,n+1):
        # fill entries of current row using previous row values
        for j in range(min(i,r),0,-1):
            C[j]=(C[j]+C[j-1])%p
    
    return C[r]

"""
Method 2: Using Pascal Triangle and Dynamic PRo

Another approach lies in utilizing the concept of the Pascal Triangle.
Instead of calculating the nCr value of every n starting from n-0 till n=n,
the approach aims at using nth row itself for the calculation. the method 
proceeds by finding out a general relationship between nCr and nCr-1

Formula:
C(n,r)=C(n,r-1)*(n-r+1)/r

"""
def moduloMultiplication(a,b,mod):
    res=0
    # update a if it is more than or equal to mod
    a%=mod

    while (b):
        # if b is odd, add a with result
        if (b&1):
            res=(res+a)%mod
        # Here we assume that doing 2*a 
        # doesn't cause overflow
        a=(2*a)%mod
        b>>=1
    
    return res

# Global variables
x,y=0,1

# Function for extended Euclidean Algorithm

def gcdExtended(a,b):
    global x,y
    # Base case 
    if (a==0):
        x=0
        y=1
        return b
    
    gcd=gcdExtended(b%a,a)
    x1=x
    y1=y

    x=y1-int(b/a)*x1
    y=x1

    return gcd

