# python program for solution of hamiltonian cycle problem

class Graph:
    def __init__(self,vertices) -> None:
        self.graph=[[0 for column in range(vertices)] for row in range(vertices)]
        self.V=vertices
    
    def isSafe(self,v,pos,path):
        if self.graph[path[pos-1]][v]==0:
            return False
        
        # check if current vertex not already in path
        for vertex in path:
            if vertex == v:
                return False
        return True
    
    # a recursive utility function to solve
    # hamiltonion cycle problem
    def hamCycleUtil(self,path,pos):
        # base case : if all vertices are
        # included in the path
        if pos == self.V:
            if self.graph[path[pos-1]][path[0]]==1:
                return True
            else:
                return False
        
        for v in range(1,self.V):
            if self.isSafe(v,pos,path)==True:
                path[pos]=v
                