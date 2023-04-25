"""
A Hoax Number is defined as a composite number,
whose sum of digits is equal to the sum of digits of its
distinc prime factors. It may be noted here that, 1 is not considered
a prime number, hence it is not included in the sum of digits of distinct
prime factors.

"""

import math 

def primeFactors(n):
    res=[]
    if (n%2==0):
        while (n%2==0):
            n=int(n/2)
        res.append(2)
    
    for i in range(3,int(math.sqrt(n)),2):
        if (n%i==0):
            while (n%i==0):
                n=int(n/i)
            res.append(i)
    if (n>2):
        res.append(i)
    return res

def isHoax(n):
    pf=primeFactors(n)

    if (pf[0]==n):
        return False 
    
    all_pf_sum=0
    for i in range(0,len(pf)):
        pf_sum=0
        while (pf[i]>0):
            pf_sum+=pf[i]%10
            pf[i]=int(pf[i]/10)
        
        all_pf_sum+=pf_sum
    
    sum_n=0
    while (n>0):
        sum_n+=n%10 
        n=int(n/10)
    
    return sum_n==all_pf_sum


