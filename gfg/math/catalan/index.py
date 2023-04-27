"""
Catalan numbers are defined as a mathematical sequence that consists of
positive integers, which can be used to find the number of possibilities of
various combinations.

The nth term in the sequence denoted Cn, is found in the following formula
(2n)!/(n+1)!(n!)

Problems with catalan number:

- Count the number of expressions containing n pairs of parentheses that
  are correctly matched.

- Count the number of possible Binary Search Trees with n keys.

- Count the number of full binary trees with n+1 leaves.

- Given a number n, return the number of ways you can draw n chords in a 
  circle with 2xn points such that no 2 chords intersect.

"""

def catalan(n):
    if n<=1:
        return 1
    
    res=0
    for i in range(n):
        res+=catalan(i)*catalan(n-i-1)
    
    return res