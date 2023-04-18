# a simple python program to check bleak number

def countSetBits(x):
    count=0
    while x:
        x=x&(x-1)
        count+=1
    return count

def isBleak(n):
    for x in range(1,n):
        if (x+countSetBits(x)==n):
            return False
    return True

def ceilLog2(x):
    count=0
    x=x-1
    while x>0:
        x=x>>1
        count+=1
    return count

def isBleak(n):
    for x in range((n-ceilLog2(n)),n):
        if (x+countSetBits(x)==n):
            return False
    return True
    