"""
Givrn an integer n and a prime number p, find the largest x such
that p^x (p raised to power x) divides n!.

n! is multiplication of {1,2,3,4,...n}.
How many numbers in {1,2,3,4,...n} are divisible by p?
Every p'th number is divisible by p in {1,2,3,4...n}. Therefore in n!, there
are [n/p] numbers divisible by p.

So we know that the value of x (largest power of p that divides n!) is at least [n/p].

Can x be larger than [n/p]?
Yes, there may be numbers which are divisible by p^2, p^3,...

How many numbers in {1,2,3,4,...n} are divisible by p^2, p^3, ...?
There are [n/p^2] numbers divisible by p^2 (Every p^2th number would be divisible). Similarly,
there are [n/p^3] numbers divisible by p^3 and so on.
"""

def largestPower(n,p):
    x=0
    while n:
        n/=p
        x+=n
    return x

"""
What to do if p is not prime?
We can find all prime factors of p and compute result for
every prime factor.

"""
def largestPower(n,p):
    if n==0:
        return 0
    
    return n//p+largestPower(n//p,p)
