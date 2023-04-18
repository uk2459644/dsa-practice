# python code to rotate bits of number

INT_BITS=32

# function to left rotate n
# by d bits

def leftRotate(n,d):
    # in n<<d, last d bits are 0
    # to put first 3 bits of n at last
    # do bitwise or of n<<d with n>>(INT_BITS-d)
    return (n<<d)|(n>>(INT_BITS-d))

# function to right rotate n by d bits
def rightRotate(n,d):
    return (n>>d)|(n<<(INT_BITS-d))& 0xFFFFFFFF
