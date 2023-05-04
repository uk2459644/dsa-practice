"""
Given N, and ff(n)=f(1)+f(2)+...+f(N), where f(k) is the sum of all subset
of a set formed by first k natural numbers. The task is to find ff(N) modulo
1000000007.

Approach: Find a pattern of the sequence that will form.
The series formed is 1,7,31,111... There exists a formula for it which is
2^n*(n^2+n+2)-1. where, N is starting from zero.

"""
mod=(int)(1e9+7)

def power(x,y,p):
    res=1
    x=x%p

    while (y>0):
        # if y is odd, multiply x with the result
        if (y&1):
            res=(res*x)%p
        y=y>>1
        x=(x*x)%p
    
    return res

def check(n):
    n=n-1 
    ans=n*n
    if (ans>=mod):
        ans%=mod
    
    ans+=n+2

    if (ans>=mod):
        ans%=mod
    
    ans = (pow(2,n,mod)%mod*ans%mod)%mod

    ans=(ans-1+mod)%mod

    return ans

