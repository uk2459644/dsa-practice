from collections import defaultdict 

# Class to represent a graph
class Graph:
    def __init__(self,vertices) -> None:
        self.V=vertices
    
    # a utility function to print the solution
    def printSolution(self,reach):
        print("Following matrix transitive closure of the graph")
        for i in range(self.V):
            for j in range(self.V):
                if (i==j):
                    print("%7d\t" %(1),end=" ")
                else:
                    print("%7d\t" %(reach[i][j]),end=" ")
            print()
    
    def transitiveClosure(self, graph):
        reach = [i[:] for i in graph]
        for k in range(self.V):
            for i in range(self.V):
                # pick all vertices as destination for the
                # above picked source
                for j in range(self.V):
                    reach[i][j]=reach[i][j] or (reach[i][k] and reach[k][j])
        
        self.printSolution(reach)

g=Graph(4)

graph= [[1,1,0,1],
        [0,1,1,0],
        [0,0,1,1],
        [0,0,0,1]]

g.transitiveClosure(graph)


    # Print transitive closure
