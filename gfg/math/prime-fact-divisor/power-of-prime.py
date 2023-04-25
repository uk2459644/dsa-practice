"""
The naive approach is to find the power of p in each
number from 1 to n and add them. Because we know that during multiplication power 
is added.
"""
def powerOfNFactorial(n,p):
    ans=0
    temp=p

    while (temp<=n):
        ans+=n/temp
        temp*=p
    
    return ans

