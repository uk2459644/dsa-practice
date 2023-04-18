# python program for solution of hamiltonian cycle problem

class Graph:
    def __init__(self, vertices) -> None:
        self.graph = [[0 for column in range(vertices)] for row in range(vertices)]
        self.V = vertices
    
    # Check if this vertex is an adjacent vertex of the
    # previously added vertex and is not included in the
    # path earlier
    def isSafe(self, v,pos,path):
        # check if current vertex and last vertex
        # in path are adjacent
        if self.graph[ path[pos-1]][v]==0:
            return False
        
        # check if current vertex not already in path
        for vertex in path:
            if vertex == v:
                return False
        
        return True
    
    def hamCycleUtil(self,path,pos):
        if pos == self.V:
            # last vertex must be adjacent to the 
            # first vertex in path to make a cycle
            if self.graph[path[pos-1]][path[0]]==1:
                return True
            else:
                return False
            

