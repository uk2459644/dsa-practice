"""
Given a number n. We need to find the number of 
ordered pairs of a and b such that gcd(A,b)
is b itself.

Naive Approach: 
gcd(a,b)=b means b is a factor of a.
So the total number of pairs will be equal to sum of
divisors for each a=1 to n.

Efficient approach: gcd(a,b)=b means that a is a multiple of b.
So the total number of apirs will be sum
of number of multiples of each b( where b varies from 1 to n) which are 
less than or equal to n.
"""

def countPairs(n):
    # initialize k
    k=n
    # loop till imin <=n
    imin=1
    # initialize result
    ans=0
    while (imin<=n):
        imax=n/k
        ans+=k*(imax-imin+1)
        imin=imax+1 
        k=n/imin
    
    return ans

