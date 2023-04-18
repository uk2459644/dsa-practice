"""
MEthod 2:

If we take a closer look at the pattern, we can find that
the count of solution is (n+1)*(n+2)/2. 

The problem is equivalent to distributing n identical balls in three
boxes and solution is n+2C2. 

In general, if there are m variables (or boxes) and n balls, the formula
becomes n+m-1Cm-1. 

"""

def countIntegralSolution(n):
    return int(((n+1)*(n+2))/2)

