# adjacency matrix reprenetation of matrix

if __name__=='__main__':
    n,m=map(int,input().split())
    adjMat=[[0 for i in range(n)] for j in range(n)]
    for i in range(n):
        u,v=map(int,input().split())
        adjMat[u][v]=1
        adjMat[v][u]=1

# a python program to demonstrate the adjacency
# list representation of the graph

class AdjNode:
    def __init__(self,data) -> None:
        self.vertex=data 
        self.next=None
# a class to represent a graph. A graph is the
# list of the adjacency lists.
# size of the array will be the no. of the
# vertices "v"
class Graph:
    def __init__(self,vertices) -> None:
        self.V=vertices
        self.graph=[None]*self.V
    
    def add_edge(self,src,dest):
        node=AdjNode(dest)
        node.next=self.graph[src]
        self.graph[src]=node

        # adding the source node to the destination as
        # it is the undirected graph
        node=AdjNode(src)
        node.next=self.graph[dest]
        self.graph[dest]=node
    
    def print_graph(self):
        for i in range(self.V):
            print("Adjacency list of vertex {}\n head".format(i),end=" ")
            temp=self.graph[i]
            while temp:
                print(" -> {}".format(temp.vertex),end=" ")
                temp=temp.next
            print(" \n")
