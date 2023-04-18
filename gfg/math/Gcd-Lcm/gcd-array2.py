# Recursive method

import math

def gcdOfArray(arr,idx):
    if idx == len(arr)-1:
        return arr[idx]
    
    a=arr[idx]
    b=gcdOfArray(arr,idx+1)

    return math.gcd(a,b)
