from collections import defaultdict, deque

class Graph:
    def __init__(self) -> None:
        self.graph=defaultdict(list)
    
    def add_edge(self,u,v):
        self.graph[u].append(v)
    
    def topological_sort_bfs(self):
        in_degree={v:0 for v in self.graph}

        for vertex in self.graph:
            for neighbor in self.graph[vertex]:
                in_degree[neighbor]+=1
        
        queue = deque([v for v in in_degree if in_degree[v]==0])
        result=[]

        while queue:
            current_vertex=queue.popleft()
            result.append(current_vertex)

            for neighbor in self.graph[current_vertex]:
                in_degree[neighbor]-=1
                if in_degree[neighbor]==0:
                    queue.append(neighbor)
            
        return result




