"""
MEthod 6:
Below is more interesting recurrence formulat that can be used
to find nth Fibonacci number in O(logn) time.

If n is even then k=n/2
F(n)=[2*F(k-1)+F(k)]*F(k)

If n is odd then k=(n+1)/2
F(n)=F(k)*F(k)+F(k-1)*F(k-1)

"""
MAX=1000

f=[0]*MAX

def fib(n):
    if n==0:
        return 0
    if (n==1 or n==2):
        f[n]=1
        return f[n]
    if f[n]:
        return f[n]
    if n&1:
        k=(n+1)//2
    else:
        k=n//2
    
    if n&1:
        f[n]=(fib(k)*fib(k)+fib(k-1)*fib(k-1))
    else:
        f[n]=(2*fib(k-1)+fib(k))*fib(k)
    
    return f[n]

# Method 7 : Binet's formula
# Fn={[(sqrt(5)+1)/2]^n}/sqrt(5)
import math 

def fibo(n):
    phi=(1+math.sqrt(5))/2
    return round(pow(phi,n)/math.sqrt(5))
    