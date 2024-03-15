from collections import defaultdict

edges = [2,2,3,-1]
node1 = 0
node2 = 1

def bfs(curr,reach):
    dst=0
    reach[curr]=0
    while edges[curr]!=-1:
        curr=edges[curr]
        dst+=1
        if curr in reach:
            break
        reach[curr]=dst
    
    return reach

reach1=bfs(node1,defaultdict(int))
reach2=bfs(node2,defaultdict(int))

result=float('inf')
result_node=-1

for node in reach1.keys():
    if node in reach2:
        if result > max(reach1[node],reach2[node]):
            result=max(reach1[node],reach2[node])
            result_node=node
        elif result == max(reach1[node],reach2[node]):
            result_node=min(node,result_node)

print(result_node)





