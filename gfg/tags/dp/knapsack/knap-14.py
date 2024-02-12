"""
Given a number n, the task is to break n in such a way that multiplication
of its parts is maximized.

Approach: 

- Define a function breakInteger that takes an integer N as input and returns
  the maximum product that can be obtained by breaking N into a sum of positive
  integers.
  - Check for the two base cases :
    - if N is 2, return 1
    if N is 3, return 2

- Define a variable maxProduct to store the maximum product
- Determine the remainder of N when divided by 3: 
   - if the remainder is 0, the maximum product is 3 raised to the power of N/3
   - if the remainder is 1, the maximum product is 2 multiplied by 3 raised to 
     the power of (N/3)-1

    - If the remainder is 2, the maximum product is 2 multiplied by 3 raised to the
      power of N/3.

Return the value of maxProduct.

"""
def power(x,a):
    res=1
    while (a):
        if (a&1):
            res=res*x
        x=x*x
        a>>=1
    
    return res

# Method returns maximum product obtained by breaking N

def breakInteger(N):
    # base case 2=1+1 
    if (N==2):
        return 1
    # base case 3=2+1 
    if (N==3):
        return 2
    maxProduct=0
    # breaking based on mod with 3
    if (N%3==0):
        # if divides evenly, then break into all 3
        maxProduct=power(3,int(N/3))
        return maxProduct
    elif(N%3==1):
        # If division give mod as 1, then break as 4+power of 3
        # for remaining part
        maxProduct=2*2*power(3,int(N/3)-1)
        return maxProduct
    elif(N%3==2):
        # if division gives mod as 2, then break as 2+power of 3
        # for remaining part
        maxProduct=2*power(3,int(N/3))
        return maxProduct
    
 
"""
Method 2- 

If we see some examples of this problems, we can easily observe following pattern.

The maximum product can be obtained be repeatedly cutting parts of size 3 while size 
is greater than 4, keeping the last part as size of 2 or 3 or 4. For example n=10, the
maximum product is obtained by 3,3,3,2. Following is the implementation of this approach:

"""

# The main function that returns max possible product

def maxProd(n):
    # n equals to 2 or 3 must be handed explicitly
    if n==2 or n==3:
        return n-1
    
    # keeps removing part of size 3 while n is greater than 4
    res=1
    while n>4:
        n-=3
        # keep multiplying 3 to res
        res*=3 
    return (n*res)



