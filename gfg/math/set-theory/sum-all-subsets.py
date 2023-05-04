"""
Given a number n, we need to find the sum of all the elements from all possible
subsets of a set formed by first n natural numbers.

A simple solution is to generate all subsets. For every subset, compute its 
sum and finally return overall sum.

An efficient solution is based on the fact that every number from 1 to n appears
exactly 2^(n-1) times. So our required sum is (1+2+3+..+n)*2^(n-1). The sum can be
written as (n*(n+1)/2)*2^(n-1).

"""
def findSumSubset(n):
    return (n*(n+1)/2)*(1<<(n-1))

