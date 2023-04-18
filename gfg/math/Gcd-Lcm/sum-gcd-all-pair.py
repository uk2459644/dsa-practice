"""
Given a number N, find sum of all GCDs that can be 
formed by selecting all the pairs from 1 to N.

Naive Approach:
A naive approach is to run two loops one inside the
other. Select all pairs one by one, find GCD of every
pair and then find sum of these GCDs.

Efficient Approach is based on following concepts:

* Euler's Totient function : -
(n) for an input n is count of numbers in {1,2,3,..,n} that are relatively
prime to n, i.e., the numbers whose GCD (Greatest Common Divisor) with n is 1.
"""