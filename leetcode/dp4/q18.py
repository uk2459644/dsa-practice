from collections import defaultdict

class Graph:
    def __init__(self) -> None:
        self.graph=defaultdict(list)
    
    def add_edge(self,u,v):
        self.graph[u].append(v)
    
    def topological_sort_util(self,v,visited:list,stack:list):
        visited[v]=True

        for neighbor in self.graph[v]:
            if not visited[neighbor]:
                self.topological_sort_util(neighbor,visited,stack)
        
        stack.append(v)
    
    def topological_sort_dfs(self):
        visited=[False]*len(self.graph)
        stack=[]

        for vertex in self.graph:
            if not visited[vertex]:
                self.topological_sort_util(vertex,visited,stack)
        
        return stack[::-1]
    
    



