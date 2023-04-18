mod=(10**9)+7

for _ in range(int(input())):
    n=int(input())
    if n>2:
        ans=pow(2,n-1,mod)-2
        print(ans)
    else:
        print(0)