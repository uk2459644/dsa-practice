n=int(input())
dic=dict()

for _ in range(n):
    si,vi=map(str,input().split(" "))
    dic[si]=int(vi)

srt=sorted(dic.items(),key=lambda x:x[1],reverse=True)

q=int(input())
for i in range(q):
    qi=input()
    find=False
    ans=''
    for sr in srt:
        if qi in sr[0]:
            find=True
            ans+=sr[0]
            continue
    if find:
        print(ans.strip())
    else:
        print("NO")
  
