"""
In number system, Sylvester's sequence is an integer sequence inwhich each
memeber of the sequence is the product of the previous memeber, plus one.

"""
def printSequence(n):
    a=1
    ans=2
    N=10**9+7 

    i=1 
    while i<=n:
        print(ans)
        ans=((a%N)*(ans%N))%N
        a=ans
        ans=(ans+1)%N
        i=i+1 
        
