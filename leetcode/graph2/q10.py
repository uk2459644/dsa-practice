
security = [1,2,3,4,5,6]
time = 2

n=len(security)

inc=[0]*n

cnt=0

prev=security[0]
for i in range(1,n):
    if prev>=security[i]:
        prev=security[i]
        cnt+=1
        inc[i]=cnt
    else:
        prev=security[i]
        cnt=0
        inc[i]=cnt

# rev_security=security[::-1]
dec=[0]*n
prev=security[-1]
cnt=0
for i in range(n-2,-1,-1):
    if prev>=security[i]:
        prev=security[i]
        cnt+=1
        dec[i]=cnt
    else:
        prev=security[i]
        cnt=0

    

# dec=dec[::-1]

ans=[]

for i in range(n):
    if inc[i]>=time and dec[i]>=time:
        ans.append(i)

print(inc,dec,ans)

