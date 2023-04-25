"""
Given three positive numbers a,b and m. Compute a/b
under modulo m. the task is basically to find a number c such that
(b*c)%m=a%m

Modular division is defined when modular inverse of the divisor exists.
The inverse of an integer 'x' is another integer y such that (x*y)%m=1
where m is the modulus.

When does inverse exist, inverse a number 'a' exists under modulo 'm'
if 'a' and 'm' are co-prime, GCD of them is 1.
"""

import math 

def modInverse(b,m):
    g=math.gcd(b,m)
    if g!=1:
        return -1
    else:
        return pow(b,m-2,m)

def modDivide(a,b,m):
    a=a%m
    inv=modInverse(b,m)
    if inv == -1:
        print("Division not defined")
    else:
        print((inv*a)%m)
