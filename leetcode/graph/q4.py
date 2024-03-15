from collections import defaultdict
import heapq

class Solution:

    def networkDelayTime(self,times:list[list[int]],n:int,k:int):
        graph=defaultdict(list)

        for u,v,w in times:
            graph[u].append((v,w))
        
        priority_queue=[(0,k)]

        shortest_path={}

        while priority_queue:
            w,v=heapq.heappop(priority_queue)
            if v not in shortest_path:
                shortest_path[v]=w
                for vi,wi in graph[v]:
                    heapq.heappush(priority_queue,(w+wi,vi))
        
        if len(shortest_path)==n:
            return max(shortest_path.values())
        else:
            return -1
            


