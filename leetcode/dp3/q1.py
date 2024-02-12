
head=list(map(int,input().split()))
k=int(input())

n=len(head)

if k>n:
    k=k%n
index=n-k
last=head[index::]
first=head[:index:]

ans=last+first
print(ans)




