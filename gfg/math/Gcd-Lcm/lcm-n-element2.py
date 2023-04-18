
def __gcd(a,b):
    if (a==0):
        return b
    
    return __gcd(b%a,a)

# recursive implementation
def lcmOfArray(arr,idx):
    # lcm(a,b)=(a*b/gcd(a,b))
    if (idx==len(arr)-1):
        return arr[idx]
    a=arr[idx]
    b=lcmOfArray(arr,idx+1)
    return int(a*b/__gcd(a,b))
