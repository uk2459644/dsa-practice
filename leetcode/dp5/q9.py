from collections import defaultdict

class Solution:
    def mostProfitablePath(self,edges:list[list[int]],
                           bob:int,amount:list[int])->int:
        
        graph = defaultdict(list)
        n=len(amount)

        for u,v in edges:
            graph[u].append(v)
            graph[v].append(u)
        
        visited=[False]*n
        bobpath=defaultdict(int)
        self.stop=False
        def bpath(node,time):
            bobpath[node]=time
            visited[node]=True
            # bob reached to root return
            if node==0:
                self.stop=True
                return
            # check if it is a leaf node
            count=0
            for nei in graph[node]:
                if not visited[nei]:
                    count+=1
            if count==0:
                del bobpath[node]
                return
            for nei in graph[node]:
                if self.stop:
                    return
                if not visited[nei]:
                    bpath(nei,time+1)
            if not self.stop:
                del bobpath[node]
            
            return
            
        return 0

