"""
A Sphenic Number is a positive integer n which is product of exactly
three distinct primes.

Sphenic number can be checked by fact that every sphenic number 
will have exactly 8 divisor.

So first we will try to find if the number is having
exactly 8 divisors if not then simply answer is no.

If there are exactly 8 divisors then we will
 confirm whether the first 3
digits after 1 are prime or not.

"""

# create a global array of size 1001
arr=[True]*(1001)

def simpleSieve():
    k=0
    for p in range(2,1001):
        if (p*p>1001):
            break
        if arr[p]:
            for k in range(p,1001,k+p):
                arr[k]=False

def find_sphene(N):
    arr1=[0]*(8)
    count=0
    j=0

    for i in range(1,N+1):
        if (N%i==0 and count<8):
            count+=1 
            arr1[j]=i
            j+=1 
    
    if (count==8 and (arr[arr1[1]] and arr[arr1[2]] and arr[arr1[3]])):
        return 1
    
    return 0

