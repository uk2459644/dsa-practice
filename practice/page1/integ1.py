
n=int(input())
a=list(map(int,input().split()))
x=int(input())
lst=[]
for i in a:
    if(i<0):
        lst.append(i)
lst.sort()
if((-sum(lst))<x):
    print(-sum(lst))
else:
    print(-sum(lst[:x]))