mod=998244353
for _ in range(int(input())):
    bstr=[a for a in input()]
    n=len(bstr)
    ali=[0]*(n+1)
    ali[0]=1
    ali[1]=1
    for i in range(1,n):
        if bstr[i]!=bstr[i-1]:
            bstr[i+1]=(bstr[i]+bstr[i-1])%mod
        else:
            ali[i+1]=ali[i]
    print(ali[n]%mod)