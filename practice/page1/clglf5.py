import bisect

for _ in range(int(input())):
    n,m=map(int,input().split())
    fli=list(map(int,input().split()))
    fli.sort()
    cli=list(map(int,input().split()))
    cli.sort()
    fbl=True
    cnt=0
    ind=0
    mn=min(fli[ind],cli[ind])
    while True:
        if mn in fli:
            if fbl==False:
                cnt+=1 
                fbl=True
                ind=bisect.bisect(cli,mn)
                if ind == m:
                    break
                mn=cli[ind-1]
        if mn in cli:
            if fbl==True:
                cnt+=1 
                fbl=False
                ind=bisect.bisect(fli,mn)
                if ind==n:
                    break
                mn=fli[ind-1]
    print(cnt)
        