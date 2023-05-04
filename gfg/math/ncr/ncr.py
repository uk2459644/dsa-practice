"""
Following are the common definitions of Binomial Coefficients.

- A binomial coefficient C(n,k) can be defined as the coefficient of
  X^k in the expansion of (1+X)^n.

- A binomial coefficient C(n,k) also gives the number of ways, disregarding
  order, that k objects can be chosen from among n objects, more formally, the
  number of kk-element subsets (or k-combinations) of an n-element set.

Approach: Below is the idea to solve the problem:

The total number of ways for selecting r elements out of n options are
nCr=(n!)/(r!*(n-r)!)
"""
def fact(n):
    if n==0:
        return 1
    
    res=1

    for i in range(2,n+1):
        res*=i
    
    return res

def ncr(n,r):
    return (fact(n)/(fact(r)*fact(n-r)))

"""
Another Approach:
The idea is to use a recursive function to calculate the value of ncr. 
The base cases are:
- if r is greater than n, return 0 (there are no combinations possible)

- if r is 0 or r is n, return 1 (there is only 1 combination possible in these cases)
"""
def ncr(n,r):
    if r>n:
        return 0
    
    if r==0 or r==n:
        return 1
    
    return ncr(n-1,r-1)+ncr(n-1,r)

