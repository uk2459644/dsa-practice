# python program to multiply any positive 
# number to 7

def multiplyBySeven(n):
    return ((n<<3)-n)

def isPowerOfTwo(x):
    return (x and (not(x&(x-1))))