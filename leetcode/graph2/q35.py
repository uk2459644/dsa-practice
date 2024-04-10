from collections import defaultdict


nums = [1,7,6,18,2,1]
limit = 3

n=len(nums)
pairs=sorted(nums)

graph= defaultdict(list)

for i in range(1,n):
    if (pairs[i]-pairs[i-1])<=limit:
        graph[nums.index(pairs[i])].append(nums.index(pairs[i-1]))
        graph[nums.index(pairs[i-1])].append(nums.index(pairs[i]))

groups=[]
visited=set()

def dfs(graph,node,visited:set,group:list):
    if node not in visited:
        group.append(node)
        visited.add(node)
        for v in graph[node]:
            dfs(graph,v,visited,group)

for node in graph:
    if node not in visited:
        group=[]
        dfs(graph,node,visited,group)
        group.sort()
        groups.append(group)
ans=[ch for ch in nums]
for group in groups:
    chars=[nums[i] for i in group]
    chars.sort()
    for i,idx in enumerate(group):
        ans[idx]=chars[i]
print(groups,ans,pairs)


