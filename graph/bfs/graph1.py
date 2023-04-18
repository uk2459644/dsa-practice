# python code to implement the approach
# function to find the level of the given node

def findLevel(N,edges,X):
    # variable to store maximum vertex of graph
    maxVertex=0
    for it in edges:
        maxVertex=max(maxVertex,max(it[0],it[1]))
    # creating adjacency list
    adj=[[] for j in range(maxVertex+1)]
    for i in range(len(edges)):
        adj[edges[i][0]].append(edges[i][1])
        adj[edges[i][1]].append(edges[i][0])
    
    # if x is not present then return -1
    if (X>maxVertex or len(adj[X])==0):
        return -1
    q=[]
    q.append(0)
    level=0
    # visited array to mark the already visited nodes
    visited=[0]*(maxVertex+1)
    visited[0]=1
    # BFS traversal 
    while (len(q)>0):
        sz=len(q)
        while(sz>0):
            cureentNode=q[0]
            q.pop(0)
            if cureentNode==X:
                return level
            for it in adj[cureentNode]:
                if (not visited[it]):
                    q.append(it)
                    visited[it]=1
            sz-=1
        level+=1
    return -1
    