"""
Given a number n, the task is to calculate its primorial.
Primorial (denoted as Pn#) is a product of first n prime numbers.
In primorial, not all the natural numbers get multiplied only prime
numbers are multiplied to calculate the primorial of a number.

A naive approach is to check all numbers from 1 to n one by one or not,
if yes then store the multiplication in result, similarly store the result
of multiplication of primes till n.

An efficient method is to find all the prime up to n
using Sieve of Sundaram and then just calculate the primorial by multiplying
them all.
"""

