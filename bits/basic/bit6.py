# count the number of bits to be flipped to convert
# a to b using the XOR operator

def countSetBits(n):
    count=0
    while n:
        count+=1
        n&=(n-1)
    return count

# function that returns count of flipped number

def flippedCount(a,b):
    return countSetBits(a^b)

def countFlips(a,b):
    flips=0
    while (a>0 or b>0):
        t1=(a&1)
        t2=(b&1)
        if (t1!=t2):
            flips+=1
        a>>=1
        b>>=1
    return flips
