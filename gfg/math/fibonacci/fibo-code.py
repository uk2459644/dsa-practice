N=30

fib=[0 for i in range(N)]

def largestFiboLessorEq(n):
    fib[0]=1
    fib[1]=2

    i=2
    while fib[i-1]<=n:
        fib[i]=fib[i-1]+fib[i-2]
        i+=1
    
    return (i-2)

def fibonacciEncoding(n):
    index=largestFiboLessorEq(n)
    codeword=['a' for i in range(index+2)]
    i=index

    while (n):
        codeword[i]='1'
        n=n-fib[i]

        while (i>=0 and fib[i]>n):
            codeword[i]='0'
            i=i-1
    
    codeword[index+1]='1'

    return "".join(codeword)