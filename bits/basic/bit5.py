# python program to find set bits in an integer

# function to get no of set bits in binary
# representation of positive integer n*/

def countSetBits(n):
    count=0
    while (n):
        count+=n&1 
        n>>=1 
    return count

def countSetBits(n):
    count=0
    while (n):
        n&=(n-1)
        count+=1
    return count
