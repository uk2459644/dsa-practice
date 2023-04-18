
"""
A left truncatable prime is a prime which in a given base
say (10) doest not contain 0 and which remains prime when
the leading ("left") digit is successively removed. For example, 317 is 
left-truncatable prime since 317,17 and 7 are all prime. There are totla 
4260 left-truncatable primes. Tha task is to check whether the given
number is left truncatable prime or not.

"""
"""
The idea is to first check whether the number contains 0 as 
a digit or not and count number of digit in the given number N. 
if it contains 0, then return alse otherwise generate all the primes
less then or equal to the given number. Once we have generated all such primes, then
we check whether the number remains prime when leading digit is successively removed.

"""

def power(x,y):
    if (y==0):
        return 1
    elif (y%2==0):
        return (power(x,y//2)*power(x,y//2))
    else:
        return (x*power(x,y//2)*power(x,y//2))

def sieveOfEratosthenes(n,isPrime):
    isPrime[0]=isPrime[1]=False
    for i in range(2,n+1):
        isPrime[i]=True 
    
    p=2 
    while(p*p<=n):
        if (isPrime[p]==True):
            i=p*2 
            while(i<=n):
                isPrime[i]=False
                i+=p 
        p+=1 

def leftTruePrime(n):
    temp=n 
    cnt=0
    while (temp!=0):
        cnt+=1 
        
