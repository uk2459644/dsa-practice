from collections import defaultdict,deque

graph=[[4,3,1],[3,2,4],[3],[4],[]]
visited=set()
paths=[]
def dfs(node,path:list):
    if len(graph[node])==0:
        paths.append(path)
    else:
        for vtx in graph[node]:
            dfs(vtx,path+[vtx])

dfs(0,[0])

print(paths)





