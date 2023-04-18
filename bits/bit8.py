# python program to rearrange array in alternating
# python program to copy set bits in a given
# range [l,r] from y to x

def copySetBits(x,y,l,r):
    if (l<1 or r>32):
        return x
    for i in range(l,r+1):
        mask=1<<(i-1)
        if ((y & mask)!=0):
            x=x|mask
    return x

def copySetBits(x,y,l,r):
    if (l<1 or r>32):
        return x
    
    masklength=(int)((1<<(r-l+1))-1)
    mask=((masklength)<<(l-1))&y
    x=x|mask
    return x

