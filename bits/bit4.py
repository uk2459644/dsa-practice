# python program to find nth magic number
# function to find nth magic number

def nthMagicNo(n):
    pow=1
    ans=0
    # go through every bit of n
    while n:
        pow=pow*5
        # if last bit of n is set
        if (n&1):
            ans+=pow
        n>>=1
    return ans

