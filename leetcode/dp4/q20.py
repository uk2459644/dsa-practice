
from collections import defaultdict

class Graph:
    def __init__(self) -> None:
        self.graph = defaultdict(list)
    
    def add_edge(self,u,v):
        self.graph[u].append(v)
    
    def is_cyclic_util(self,v,visited:list,recursion_stack:list):
        visited[v]=True
        recursion_stack[v]=True

        for neighbor in self.graph[v]:
            if not visited[neighbor]:
                if self.is_cyclic_util(neighbor,visited,recursion_stack):
                    return True
                elif recursion_stack[neighbor]:
                    return True
        
        recursion_stack[v]=False
        return False
    
    def is_cyclic_dfs(self):
        visited=[False]*len(self.graph)
        recursion_stack=[False]*len(self.graph)

        for vertex in self.graph:
            if not visited[vertex]:
                if self.is_cyclic_util(vertex,visited,recursion_stack):
                    return True
        
        return False
    


