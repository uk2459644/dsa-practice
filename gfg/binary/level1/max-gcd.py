# Program to find the maximum
# GCD of the siblings of a binary tree

from math import gcd

# funnction to find maximum GCD

def max_gcd(v):
    # no child or sibling child
    if (len(v) == 1 or len(v)==0):
        return 0
    
    v.sort()
    # To get the first pair
    a=v[0]
    ans=-10**9
    for i in range(1,len(v)):
        b=v[i]
        # If both the pairs belongs to 
        # the same parent 
        if (b[0]==a[0]):
            ans=max(ans,gcd(a[1],b[1]))
        a=b 
    
    return ans


