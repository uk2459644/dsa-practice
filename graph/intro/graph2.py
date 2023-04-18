# python program to find transpose of a graph
# function to add an edge from vertex
# source to vertex dest

def addEdge(adj,src,dest):
    adj[src].append(dest)

def displayGraph(adj,v):
    for i in range(v):
        print(i,"-->",end=" ")
        for j in range(len(adj[i])):
            print(adj[i][j],end=" ")
        print()

# function to get transpose of a graph
# taking adjacency list of given graph
# and that of transpose graph
def transposeGraph(adj,transpose,v):
    for i in range(v):
        for j in range(len(adj[i])):
            addEdge(transpose,adj[i][j],i)