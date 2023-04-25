"""
Factorial of a non-negative integer is the multiplication
of all positive integers smaller than or equal to n.

"""
def factorial(n):
    if n==0:
        return 1
    
    return n*factorial(n-1)
"""
Iterative Solution to find factorial of a number:

Approach 1: Using for loop

"""
def factorial(n):
    res=1
    for i in range(2,n+1):
        res*=i
    
    return res

# Using while loop
def factorial(n):
    if n==0:
        return 1
    i=n
    fact=1

    while (n/i!=n):
        fact=fact*i
        i-=1
    
    return fact
