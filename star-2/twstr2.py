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
        if sr[0].startswith(qi):
            find=True
            ans=sr[0]
            break
    if find:
        print(ans.strip())
        ans=''
    else:
        print("NO")
  
