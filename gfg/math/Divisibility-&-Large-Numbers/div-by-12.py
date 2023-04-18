# If a number is divisible by 4 and 3
# then it is divisible by 12

import math 

def isDivisibleBy12(num):
    # if number greater than 3
    if (len(num)>=3):
        # find last digit 
        d1=int(num[len(num)-1])
        # num is odd
        if (d1%2!=0):
            return False 
        # find second last digit
        d2 = int(num[len(num)-2])
        # find sum of all digits 
        sum = 0
        for i in range(0,len(num)):
            sum+=int(num[i])
        
        return (sum%3==0 and (d2*10 + d1)%4==0)
    else:
        number = int(num)
        return (number%12==0)
    