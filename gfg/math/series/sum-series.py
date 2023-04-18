"""
Python code to find sum of series 
2, 22, 222, ..

"""
import math 

# function which return 
# the sum of series 

def sumOfSeries(n):
    return 0.02469*((10*math.pow(10,n)-1)-(9*n))
