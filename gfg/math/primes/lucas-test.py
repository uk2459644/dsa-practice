"""
A number p greter than one is prime if and only if
the only divisors of p are 1 and p. First few prime 
numbers are 2,3,5,7,11,13, ...

The lucas test is a primality test for a natural number n,
it can test primality of any kind of number.

Lucas TEST: 

A positive number n is prime if there exists an integer a(1<a<n) such
that:

a^(n-1)=1(mod n)

Problem Associated with Lucas's test are: 
- Knowing all of the prime factors of n-1 
- Finding an appropriate choice for a
"""

import random 
import math 

def primeFactors(n, factors):
    if (n%2==0):
        factors.append(2)
    
    while (n%2==0):
        n=n//2 
    for i in range(3,int(math.sqrt(n))+1,2):
        if (n%i==0):
            factors.append(i)
        while (n%i==0):
            n=n//i 
    
    if (n>2):
        factors.append(n)
    
    return factors 

def power(n,r,q):
    total=n
    for i in range(1,r):
        total=(total*n)%q 
    
    return total 

def lucasTest(n):
    if (n==1):
        return "neither prime nor composite"
    if (n==2):
        return "prime"
    if (n%2==0):
        return "composite1"
    
    factors=[]
    factors=primeFactors(n-1,factors)
    rand=[i+2 for i in range(n-3)]

    random.shuffle(rand)
    for i in range(n-2):
        a=rand[i]

        if (power(a,n-1,n)!=1):
            return "composite"
        
        # This is to check if every factor of n-1 satisfy 
        # the condition
        flag=True 
        for k in range(len(factors)):
            if (power(a,(n-1)//factors[k],n)==1):
                flag=False 
                break
        
        if flag:
            return "prime"
    
    return "probably composite"
