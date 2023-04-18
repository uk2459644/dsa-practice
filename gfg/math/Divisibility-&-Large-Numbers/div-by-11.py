# A number is divisible by 11 if difference of following
# two is divisible by 11
# 1. sum of digits at odd places 
# 2. sum of digits at even places 

def check(st):
    n=len(st)

    # compute sum of even and odd digit
    # sum
    oddDigitSum = 0
    evenDigSum = 0

    for i in range(0,n):
        # When i is even, position of digits is odd
        if (i%2==0):
            oddDigitSum+=((int)(st[1]))
        else:
            evenDigSum+=((int)(st[i]))

    return ((oddDigitSum - evenDigSum)%11 == 0)
