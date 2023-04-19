"""
A smith number is a composite number whose sum of digit is equal to the
sum of digits in its prime factorization.

"""
import math

MAX=10000
# utility function for sieve of sundaram
def sieveSundaram ():
    #In general Sieve of Sundaram, produces primes smaller
    # than (2*x + 2) for a number given number x. Since
    # we want primes smaller than MAX, we reduce MAX to half
    # This array is used to separate numbers of the form
    # i+j+2ij from others where 1 <= i <= j
    marked  = [0] * ((MAX/2)+100)
    # Main logic of Sundaram. Mark all numbers which
    # do not generate prime number by doing 2*i+1
    i = 1
    while i <= ((math.sqrt (MAX)-1)/2) :
        j = (i* (i+1)) << 1
        while j <= MAX/2 :
            marked[j] = 1
            j = j+ 2 * i + 1
        i = i + 1
    # Since 2 is a prime number
    primes.append (2)
     
    # Print other primes. Remaining primes are of the
    # form 2*i + 1 such that marked[i] is false.
    i=1
    while i <= MAX /2 :
        if marked[i] == 0 :
            primes.append( 2* i + 1)
        i=i+1
 
#Returns true if n is a Smith number, else false.
def isSmith( n) :
    original_no = n
     
    #Find sum the digits of prime factors of n
    pDigitSum = 0;
    i=0
    while (primes[i] <= n/2 ) :
         
        while n % primes[i] == 0 :
            #If primes[i] is a prime factor ,
            # add its digits to pDigitSum.
            p = primes[i]
            n = n/p
            while p > 0 :
                pDigitSum += (p % 10)
                p = p/10
        i=i+1
    # If n!=1 then one prime factor still to be
    # summed up
    if not n == 1 and not n == original_no :
        while n > 0 :
            pDigitSum = pDigitSum + n%10
            n=n/10
       
    # All prime factors digits summed up
    # Now sum the original number digits
    sumDigits = 0
    while original_no > 0 :
        sumDigits = sumDigits + original_no % 10
        original_no = original_no/10
         
    #If sum of digits in prime factors and sum
    # of digits in original number are same, then
    # return true. Else return false.
    return pDigitSum == sumDigits
#-----end of function isSmith------
 
#Driver method
# Finding all prime numbers before limit. These
# numbers are used to find prime factors.
sieveSundaram();
print "Printing first few Smith Numbers using isSmith()"
i = 1
while i<500 :
    if isSmith(i) :
        print i,
    i=i+1