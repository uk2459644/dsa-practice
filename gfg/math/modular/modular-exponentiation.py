"""
Efficient Approach:
The problem with the above solution is, overflow may occur.

(ab)mod p = ((a mod p)(b mod p)) mod p
"""

def power(x,y,p):
    x=x%p
    if (x==0):
        return 0
    
    while (y>0):
        if ((y&1)==1):
            res=(res*x)%p
        y=y>>1
        x=(x*x)%p
    
    return res
