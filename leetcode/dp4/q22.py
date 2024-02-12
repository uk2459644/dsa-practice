from collections import deque

class Solution:
    def nodeLevel(self,V,adj,X):
        level=0
        visited=[False]*V
        queue=deque([0])
        visited[0]=True
        while queue:
            curr_len=len(queue)
            for _ in range(curr_len):
                vtx=queue.popleft()
                if vtx==X:
                    return level
                for v in adj[vtx]:
                    if not visited[v]:
                        queue.append(v)
                        visited[v]=True
            level+=1
        
        return -1
                


