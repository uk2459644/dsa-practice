from collections import defaultdict

n=0
tasks = ["A","A","A","A","A","A","B","C","D","E","F","G"]
taskdic=defaultdict(int)
for c in tasks:
    taskdic[c]+=1
left = list(taskdic.keys())
right=[]
ans=0
while True:
    count=0
    for c in left:
        if count <= n and taskdic[c]>0:
            taskdic[c]-=1
            count+=1
            ans+=1
            if taskdic[c]==0:
                right.append(c)
    if count==0 or len(left)==len(right):
        break
    if count < n+1:
        ans+=(n+1-count)
    

print(ans)




