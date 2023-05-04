"""
Given a number N, the task is to find the product of all the elements from all
possible subsets of a set formed by first N natural numbers.

Naive Approach: A simple solution is to generate all subsets of first N natural.
Then for every subset, compute its product and finally return overall
product of each subset.

Effiecient Approach: 

- It can be observed that each element of the original array appears in 2^(n-1)
  times in all subsets.

- Therefore contribution of any element arri in the final answer will be
   i*2^(n-1)

- So, the sum of cubes of all subsets will be, 
  1^(2n-1)*2^(2n-1)*3^(2n-1)...N^(2n-1)

"""

def product(N):
    ans=1
    val=2**(N-1)

    for i in range(1,N+1):
        ans*=(i**val)
    
    return ans
