
def get_inds(arr,a):
    al=list()
    for it in range(len(arr)):
        if  arr[it]==a and len(al)<a:
            al.append(it)
        elif len(al)>=a:
            break
    return al

for _ in range(int(input())):
    n=int(input())
    bli=list(map(int,input().split()))
    ali=[0]*n
    ind_n=n-1
    num=1
    if max(bli)>n or (len(bli)>n):
        print(-1)
    else:
        for b in bli:
            if b >0:
                inds=get_inds(bli,b)
                for ind in inds:
                    bli[ind]=0
                    ali[ind]=num
                num+=1
            elif b==1:
                ind=bli.index(b)
                bli[ind]=0
                ali[ind]=num
                num+=1
        print(*ali)
    