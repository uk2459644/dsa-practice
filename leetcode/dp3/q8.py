
s=input()
sli=list(map(str,input().split()))

n=len(sli)

def solve(i,sn):
    if len(sn)==0:
        return True
    if i==n:
        return False
    ans1,ans2=False,False
    if sli[i] in sn:
        sng=sn.replace(sli[i],"")
        print(sng,len(sng))
        ans1=solve(i+1,sng)
    ans2=solve(i+1,sn)

    return ans1 or ans2
ans=solve(0,s)
print(ans,s)



