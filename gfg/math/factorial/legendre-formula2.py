import sys

def findPowerOfP(n,p):
    count=0
    r=p

    while (r<=n):
        count+=(n//r)
        r=r*p
    
    return count

def primeFactorsofK(k):
    ans=[]
    i=2

    while k!=1:
        if k%i ==0:
            count=0
            while k%i==0:
                k=k//i
                count+=1
            ans.append([i,count])
        i+=1
    return ans

