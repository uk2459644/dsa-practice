"""
This code uses the reduce function from the functools library and 
and the gcd function from the math
library to find the LCM of a list of numbers. The reduce function
applies the lambda function to the elements of the list, cumulatively
reducing the list to a single value (the LCM in this case). The 
lambda function calculates the LCM of two numbers using the same 
approach as the previous implementation. The final LCM is returned as the result

"""

from functools import reduce
import math 

def lcm(numbers:list):
    return reduce(lambda x,y:x*y//math.gcd(x,y),numbers,1)
