
from collections import defaultdict, deque

class Graph:
    def __init__(self) -> None:
        self.graph = defaultdict(list)
    
    def add_edge(self,u,v):
        self.graph[u].append(v)
    
    def is_cyclic_bfs(self):
        visited = [False]*len(self.graph)
        queue = deque()

        for vertex in self.graph:
            if not visited[vertex]:
                queue.append((vertex,-1))

                while queue:
                    current_vertex,parent_vertex=queue.popleft()
                    visited[current_vertex]=True

                    for neighbor in self.graph[current_vertex]:
                        if not visited[neighbor]:
                            queue.append((neighbor,current_vertex))
                        elif neighbor != parent_vertex:
                            return True
        
        return False
    



