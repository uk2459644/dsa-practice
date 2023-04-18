# python program for the above approach
# this function swaps bit at positions p1 and p2
# in an integer

def swapBits(n,p1,p2):
    bit1=(n>>p1)&1
    bit2=(n>>p2)&1

    x=(bit1^bit2)
    x=(x<<p1)|(x<<p2)
    result=n^x
    return result
    