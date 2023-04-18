"""
It is basically a function with domain and co-domain as
natural numbers and 0. It is recursively defined as below.

Specifically, let a(n) denote the (n+1)-th term. (0 is alreaady there.)
The rule says:

a(0)=0

if n>0 and the number is not already included in sequence:
    a(n)=a(n-1)-n
else: 
  a(n)=a(n-1)+n

"""
def recman(n):
    arr=[0]*n 
    # first term of the sequence is always 0
    arr[0]=0
    print(arr[0], end=", ")

    # Fill remaining terms using recursive formula
    for i in range(1,n):
        curr = arr[i-1]-i 
        for j in range(0,i):
            # if element is negative or already exists
            if ((arr[j]==curr) or curr<0):
                curr = arr[i-1]+i 
                break 
        
        arr[i]=curr 
        print(arr[i], end=", ")
        