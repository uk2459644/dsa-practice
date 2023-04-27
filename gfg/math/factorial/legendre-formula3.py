import math

def largestPower(n,k):
    factors={}
    i=2
    while i*i<=k:
        while k%i==0:
            if i in factors:
                factors[i]+=1
            else:
                factors[i]=1
            k//=i
        i+=1
    if k>1:
        if k in factors:
            factors[k]+=1
        else:
            factors[k]=1
    
    minPower=math.inf

    for p,a in factors.items():
        power=0
        i=p

        while i<=n:
            power+=n//i
            i*=p
        
        minPower=min(minPower,power//a)
    
    return minPower

