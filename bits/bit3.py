# python program to swap even and odd
# bits of a given number

def swapBits(x):
    # get all even bits of x
    even_bits=x & 0xAAAAAAAA
    odd_bits=x&0x55555555
    # right shift even bits
    even_bits>>=1
    # left shift odd bits
    odd_bits<<=1
    return (even_bits|odd_bits)

def swapBits(x):
    for i in range(0,32,2):
        # find ith bit
        ibit=(x>>1)&1
        # find i+1 th bit
        i_1_bit=(x>>(i+1))&1
        x=x-(ibit<<i)-(i_1_bit<<(i+2))+(ibit<<(i+1))+(i_1_bit<<i)
    return x