"""
The task is to find the difference in length of the shortest and second
shortest paths from node 1 to N. If the second shrtest path does not exist, print 0.
"""

def dfs(graph,s,e,v,count,dp):
    if s==e:
        # push  the number of nodes required for one of the 
        # possible paths
        dp.append(count)
        return
    
    for i in graph[s]:
        if v[i]!=1:
            # mark the node as visited and call the function to search
            # for possible paths and unmark the node.
            v[i]=1
            dfs(graph,i,e,v,count+1,dp)
            v[i]=0

# function to find the difference between the shortest and second shortest
# path

def findDifference(n,m,arr):
    # construct the graph
    graph=[]
    for i in range(n):
        graph.append([])
    
    for i in range(m):
        a=arr[i][0]
        b=arr[i][1]

        graph[a-1].append(b-1)
        graph[b-1].append(a-1)
    # vector to mark the nodes as visited or not
    v=[0]*n
    # vector to store the count of all possible paths
    dp=[]
    # mark the starting node as visited
    v[0]=1
    # function to find all possible paths
    dfs(graph,0,n-1,v,0,dp)
    # sort the vector
    dp.sort()

    # print the difference
    if (len(dp)!=1):
        print(dp[1]-dp[0],end=" ")
    else:
        print(0)
