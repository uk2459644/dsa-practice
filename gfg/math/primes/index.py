"""
A prime number is defined as a natural number
greater than 1 and is divisible by only 1 and itself.

The remaining numbers, except for 1, are classified as prime and composite numbers.

Some interesting facts about Prime Numbers:

- Except for 2, which is the smallest prime number and the
only even prime number, all prime numbers are odd numbers.

- Every prime number can be represented in form of 6n+1 or 6n-1 except
 the prime numbers 2 and 3, where n is any natural number.

 - 2 and 3 are only two consecutive natural numbers that are prime.
 - Goldbach Conjecture: Every even integer greater than 2 can be expressed as the
  sum o two primes.
 - Wilson's theorem states that a natural number p>1 is a prime number is 
  and only if
  (p-1)!=-1 mod P 
  (p-1)!=(p-1)mod p

  Properties of Prime Numbers:
  * Every number greater than 1 can be divided by at least one prime
    number.
  * Every even positive integer greater than 2 can be expressed as the 
    sum of two primes.
  * Except 2, all other prime numbers are odd. In other words, we can say that 2
    is the only even prime number.
  * Two prime numbers are always coprime to each other.
  * Each composite number can be factored into prime factors and
    individually all of these are unique in nature.
  
 Prime Numbers and Co-prime numbers:
 It is important to distinguish between prime numbers and co-prime numbers.
 Listed below are the differences between prime and co-prime numbers.

 * Coprime numbers are always considered as a pair,
   whereas a prime number is a single number.
 * Co-prime numbers are numbers that have no common factor except 1. In contrast,
   prime numbers do not have such condition.
 A co-prime number can be either prime or composite, but its greatest common factor
 (GCF) must always be 1.

 Unlike composite numbers, prime numbers have only two factors, 1 and the number itself.

"""

"""
Check a number is prime or not? 

Iterate from 2 to (n-1) and check if any number in this range divides n.
If the number divides n, then it is not a prime number.

"""

def isPrime(n,i):
    # Corner case
    if (n==0 or n==1):
        return False
    if (n==i):
        return True 
    if (n%i==0):
        return False 
    i+=1 
    return isPrime(n,i)
