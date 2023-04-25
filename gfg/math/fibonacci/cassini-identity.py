"""
Given a number N, the task is to evaluate below expression.
f(n-1)*f(n+1)-f(n)*f(n)

Cssini's identity:
f(n-1)*f(n+1)-f(n*n)=(-1)^n

So, we don't need to clculate any fibonacci term, the only thing
is to check whether n is even or odd.
"""
def cassini(n):
    return -1 if (n&1) else 1
