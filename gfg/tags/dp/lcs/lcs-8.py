"""
Length of longest common prime subsequence from two given arrays

Efficient Approach: 

The idea is to find all the prime numbers from both the arrays and then 
find the longest common prime subsequence from them using Dynamic Programming.
Follow the steps below to solve the problem: 

1. Find all the prime numbers between the minimum element of the array
  and maximum element of the array using Sieve of eratosthenes algorithm.
2. Store the sequence of primes from the arrays arr1[] and arr2[]

3. Find the LCS of the two sequence of primes.

"""

def recursion(arr1,arr2,i,j,dp):
    if i>=len(arr1) or j>= len(arr2):
        return 0
    

