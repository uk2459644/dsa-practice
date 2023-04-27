"""
Approach 2: using Stirling's approximation formula to calculate
the factorial and logarithm to count the number of digits.

"""
import math

def countDigitsInFactorial(n):
    if n<0:
        return 0
    if n<=1:
        return 1
    
    x=(n*math.log10(n/math.e)+math.log10(2*math.pi*n)/2.0)

    return math.floor(x)+1 

