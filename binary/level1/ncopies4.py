def solve():
    n,m=map(int,input().split())
    b=input()
    if b.count('1')==0:
        print(n*m)
    elif b.count("1")%2==1:
        if m%2==1:
            print(0)
        else:
            ans=0
            for i in range(n):
                if b[i]=="1":
                    break
                ans+=1
            for i in range(n-1,-1,-1):
                if b[i]=="1":
                    break
                ans+=1 
            print(ans+1)
    else:
        if m%2==1:
            suff = b.count("1")
            pre = 0
            ans = 0
            for i in range(n):
                if b[i]=="1":
                    suff-=1
                    pre+=1
                if pre == suff:
                    ans+=1 
            print(ans)
        else:
            ans=0
            for i in range(n):
                if b[i]=="1":
                    break
                ans+=1
            for i in range(n-1,-1,-1):
                if b[i]=="1":
                    break
                ans+=1
            print(ans+1)

for t in range(int(input())):
    solve()