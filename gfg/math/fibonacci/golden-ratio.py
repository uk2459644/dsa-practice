"""
Another simple way of finding nth Fibonacci number is using golden ratio as
Fibonacci numbers maintain approximate golden ratio till infinite.
ratio=(1+sqrt(5))/2=1.6180339887..

Fn=round(Fn-1*ratio)

Till 4th term, ratio is not much close to golden ratio. So, we will consider from 5th
term to get next fibonacci number.
"""
PHI=1.6180339

f=[0,1,1,2,3,5]

def fib(n):
    if n<6:
        return f[n]
    t=5
    fn=5
    while t<n:
        fn=round(fn*PHI)
        t+=1
    return fn



