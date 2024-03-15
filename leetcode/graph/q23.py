from collections import deque

parents=[]
n=len(parents)

degree=[0]*n

for p in parents:
    if p!=-1:
        degree[p]+=1

q=deque(i for i,d in enumerate(degree) if d==0)

num_kids = [0]*n
score = [1]*n

max_score,count=0,0

while q:
    i=q.popleft()
    if i!=0:
        score[i]*=(n-num_kids[i]-1)
        degree[parents[i]]-=1

        if degree[parents[i]]==0:
            q.append(parents[i])
        
    score[parents[i]]*=num_kids[i]+1
    num_kids[parents[i]]+=num_kids[i]+1

    if score[i]>max_score:
        max_score=score[i]
    elif score[i] == max_score:
        count+=1

print(count)


