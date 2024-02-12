"""
A Naive Python recursive implementation
of LIS problem 

To make use of recursive calls, this function must return
two things: 
1-> Length of LIS ending with element arr[n-1]
"""

import sys

def f(idx,prev_idx,n,a,dp):
    if idx==n:
        return 0
    

