"""
Python code to print first k digits of 1/n
where n is a positive integer

"""

import math 

def print(n,k):
    rem=1 
    for i in range(0,k):
        # the next digit can always be 
        # obtained as doing 
        # (10*rem)/10
        print(math.floor(((10*rem)/n)),end="")

        rem=(10*rem)%n 
        