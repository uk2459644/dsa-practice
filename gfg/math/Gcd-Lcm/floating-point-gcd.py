"""
Express each of the numbers without decimals.
"""

import math

def gcd(a,b):
    if (a<b):
        return gcd(b,a)
    # base case
    if (abs(b)<0.001):
        return a 
    else:
        return (gcd(b,a-math.floor(a/b)*b))
    
    