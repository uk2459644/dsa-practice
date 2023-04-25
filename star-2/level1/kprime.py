
def countPrime(n):
    count=0
    i=2
    while i*i<=n:
        if n%i:
            i+=1 
            count+=1 
        else:
            n//=i
    
    return count
for _ in range(int(input())):
    a,b,k=map(int,input().split())
    kcount=0
    for i in range(a,b+1):
        kprime=countPrime(i)
        if kprime == k:
            kcount+=1 
    
    print(kcount)

    