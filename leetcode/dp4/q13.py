from collections import defaultdict

s="cocgcickmlmsmtbwbxoz"
chars=defaultdict(int)
for ch in s:
    chars[ch]+=1
items=sorted(chars.items(),key= lambda x:x[1],reverse=True)
sng=""
for key,val in items:
    sng+=key*val
ans=""
n=len(s)
for i in range(n//2):
    if sng[i]==sng[-(i+1)]:
        print(ans)
    ans+=sng[i]
    ans+=sng[-(i+1)]
if n%2!=0:
    if ans[-1]==sng[n//2]:
        print(ans)
    ans+=sng[n//2]
print(ans)
   


