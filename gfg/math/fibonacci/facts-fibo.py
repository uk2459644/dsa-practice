"""
PAttern in LAst digits of fibonacci numbers:
The series of last digits repeats with a cycle length of 60.
"""
def fun():
    max=100
    arr=[0 for i in range(max)]
    arr[0]=0
    arr[1]=1

    for i in range(2,max):
        arr[i]=arr[i-1]+arr[i-2]
    
    for i in range(1,max-1):
        if ((arr[i]%10==0) and (arr[i+1]%10==1)):
            break
"""
2. Factors of Fibonacci number: We can observe the following thing:
- Every 3-rd fibonacci number is a multiple of 2
- Every 4-th fibonacci number is a multiple of 3
- Every 5-th fibonacci number is a multiple of 5
- Every 6-th fibonacci number is a multiple of 8
"""

"""
4. Value of f(n-1)*f(n+1)-f(n)*f(n) is (-1)^n

5. The sum of any ten consecutive Fibonacci numbers is divisible by 11

"""
