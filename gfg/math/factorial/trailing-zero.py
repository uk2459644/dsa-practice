"""
Given an integer n, write a function that returns count of trailing
zeroes in n!.

Approach 1:
A simple method is to first calculate factorial of n,
then count trailing 0s in the result (We can count trailing 0s by repeatedly
dividing the factorial by 10 till the remainnder is not 0).

Approach 2:
The above method can cause overflow for slightly bigger numbers as the
factorial of a number is a big number. The idea is to consider prime factors
of a factorial n. A trailing zero is always produced by prime factors 2 nd 5.
If we can count the number of 5s and 2s, our task is done. Consider the following
examples:- 

n=5: There is one 5 and 3s 2s in prime factors of 5!. So a count of trailing
0s is 1.

- We can easily observe that the number of 2s in prime factors is always more
  than or equal to the number of 5s. So if we count 5s in prime factors, we are
  done.

  How to count the total number of 5s in prime factors of n! A simple way is
  to calculate floor(n/5).
  mathmatically:
  =floor(n/5)+floor(n/25)+floor(n/125)+...

"""
def findTrailingZeros(n):
    if (n<0):
        return -1
    
    count=0

    while(n>=5):
        n//=5
        count+=n
    
    return count
"""
Approach 2:
Counting the number of factors of 10, another way to count the number
of trailing zeroes in the factorial of a number is to count the numbers of
factors of 10 in that number's factorial. This is because a trailing zero is
added to the factorial every  time a factor of 10 is encountered.

"""

def countTrailingZeroes(n):
    count=0
    for i in range(1,n+1):
        j=1
        while j%5==0:
            count+=1
            j//=5
    
    return count

