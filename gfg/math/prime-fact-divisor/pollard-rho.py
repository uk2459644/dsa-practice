"""
Cooncepts used in Pollard's Rho Algorithm

1. Two numbers x and y are sid to be congurent modulo 
n(x=y modulo n) if 
   - their absolute difference is an integer multiple of n, OR
   - each of them leaves the same remainder when divided by n.

2. The Greatest Common Divisor is the largest number which divides evenly
   into each of the original numbers.

3. Birthday Paradox: The probability of two persons having same birthday is unexpectedly
   high even for small set of people.

4. Floyd's cycle-finding algorithm: If tortoise and here start at same point and move
   in a cycle such that speed of hare is twice the speed of tortoise, then they must
   meet at some point.

"""
"""
Algorithm:
1.Start with random x and c. Take y equal to x and f(x)=x^2 + c
"""
import random 
import math 

def modular_pow(base,exponent,modulus):
    result=1
    while (exponent>0):
        # if y is odd, multiply bse with result
        if (exponent & 1):
            result=(result*base)%modulus
        exponent=exponent>>1 
        base=(base*base)%modulus
    return result

def PollardRho(n):
    # no prime divisor for 1
    if (n==1):
        return n
    
