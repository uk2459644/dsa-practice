from queue import Queue
from typing import List

class KnapsackNode:
    def __init__(self,items:List[int],value:int,weight:int) -> None:
        self.items=items
        self.value=value
        self.weight=weight
        

class Item:
    def __init__(self,value:int,weight:int) -> None:
        self.value=value
        self.weight=weight
        self.ration=value/weight

class KnapSack:
    def __init__(self,maxWeight:int,items:List[Item]) -> None:
        self.maxWeight=maxWeight
        self.items=items

    def solve(self)->int:
        self.items.sort(key=lambda x:x.ration, reverse=True)
        bestValue=0
        queue=[KnapsackNode([],0,0)]

        while queue:
            node=queue.pop(0)
            i=len(node.items)
            


