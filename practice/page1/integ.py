n=int(input())
nli=list(map(int,input().split()))
x=int(input())
if x>0:
    nli=list(filter(lambda a:a<0,nli))
    ans=0
    mn=int(abs(max(nli)))
    ans_sm=int(abs(sum(nli)))
    cnt=(mn*x)
    while ans_sm>cnt and len(nli)>1:
        ans+=cnt
       # print(ans,ans_sm,cnt)
        nli=list(map(lambda a:a+mn,nli))
        nli=list(filter(lambda b:b<0,nli))
        mn=int(abs(max(nli)))
        ans_sm=int(abs(sum(nli)))
        cnt=(mn*x)
    ans+=int(abs(sum(nli)))
    print(ans)
else:
    print(int(abs(sum(nli))))
