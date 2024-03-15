import sys

class Graph:
    def __init__(self,vertices):
        self.V = vertices
        self.graph=[[0 for column in range(vertices)] for row in range(vertices)]
    
    # A utility function to print the constructed MST stored in parent
    def printMST(self,parent):
        print("Edge \tWeight")
        for i in range(1,self.V):
            print(parent[i],"-",i,"\t",self.graph[i][parent[i]])
    
    # A utility function to find the vertex with
    # the minimum key value, from the set of vertices
    # not yet included in the MST
    def minKey(self,key,mstSet):
        min=sys.maxsize
        for v in range(self.V):
            if key[v] < min and mstSet[v]==False:
                min=key[v]
                min_index=v
        
        return min_index
    
    # Function to construct and print MST for a graph represented
    # using adjacency matrix representation
    def primMSt(self):
        # Key values used to pick minimum weight edge in cut
        key=[sys.maxsize]*self.V
        parent=[None]*self.V
        # make key 0 so that vertex is picked as first vertex
        key[0]=0
        mstSet=[False]*self.V
        # First node is always the root of
        parent[0]=-1

        for cout in range(self.V):
            # pick the minimum key vertex from the set of 
            # vertices not yet included in MST
            u=self.minKey(key,mstSet)
            # Add the picked vertex to the MST set
            mstSet[u]=True

            # update the key value and parent index of the
            # adjacent vertices of the picked vertex
            # consider only those vertices which are not yet 
            # included in the MST
            for v in range(self.V):
                # graph[u][v] is non-zero only for adjacent vertices of matrix
                # mstSet[v] is false for vertices not yet included in MST
                # update the key only if graph[u][v] is smaller than key[v]
                if self.graph[u][v]>0 and mstSet[v]==False and key[v]>self.graph[u][v]:
                    key[v]=self.graph[u][v]
                    parent[v]=u
        



