"""
Given two numbers, fact and n, find the largest power of n that divides
fact!

The idea is based on Legendre's formula. We find all prime factors of n.
For every prime factor we find largest power of it that divides fact!.
Finally we return minimum of all found powers.

"""

import math

def findPowerPrime(fact,p):
    res=0
    while fact:
        res+=fact//p
        fact//=p
    
    return res

def findPowerComposite(fact,n):
    res=math.inf

    for i in range(2,int(n**0.5)+1):
        count=0
        if not n%i:
            count+=1
            n=n//i
        
        if count:
            curr_pow=findPowerPrime(fact,i)//count
            res = min(res,curr_pow)
    
    if n>=2:
        curr_pow=findPowerPrime(fact,n)
        res=min(res,curr_pow)
    
    return res

"""
Approach 2:
The maximum power of a number p that divides n! is the sum of the
quotients of n divided by successive powers of p, upto the largest power
of p that divides n. More formally, we can write:

max_power=floor(n/p)+floor(n/p^2)+floor(n/p^3)+...+floor(n/p^k)

where k is the largest integer such that p^k divides n.

Here we first read in the values of n and p. then, we initialize the max
power to 0 and the power of p to pk=p. We iterate over all powers of p
that are less than or equal to n, and at each iteration we add floor(n/pk)
to the maximum power and multiply pk by p.
"""

n=146
p=5

max_power=0
pk=p

while pk<=n:
    max_power+=n//pk
    pk*=p
    

