# Python program for the above approach

# function to add edges
def addEdge(adj,u,v):
    adj[u].append(v)

# function to print adjacency list
def adjacencylist(adj,V):
    for i in range(0,V):
        print(i,"->",end="")

        for x in adj[i]:
            print(x," ",end=" ")
        print()

# function to initialize the adjacency list
# of the given graph

def initGraph(V, edges, noOfEdges):
    adj=[0]*3
    for i in range(0,len(adj)):
        adj[i]=[]
    # Traverse edges array and make edges
    for i in range(0,noOfEdges):
        # function call to make an edge
        addEdge(adj,edges[i][0],edges[i][1])

    # function call to print adjacency list
    adjacencylist(adj,V)

# Driver code
# given vertices
V=3
# given edges
edges = [[0,1],[1,2],[2,0]]
noOfEdges=3
# function call
initGraph(V,edges,noOfEdges)