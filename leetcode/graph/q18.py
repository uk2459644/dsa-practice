
class Solution:
    def closeMeetingNode(self,edges:list[int],node1:int,node2:int):
        visited_1=set()
        visited_2=set()

        while node1 !=-1 or node2 != -1:
            # record only if node is not cyclic or not at its destination
            if node1 !=-1 and node1 not in visited_1:
                if node1 in visited_2:
                    if node2 in visited_1:
                        return min(node1,node2)
                    return node1
                visited_1.add(node1)
                node1=edges[node1]
            
            if node2 !=-1 and node2 not in visited_2:
                if node2 in visited_1:
                    return node2
                visited_2.add(node2)
                node2=edges[node2]
            
            if (node1 in visited_1 or node1==-1) and (node2 in visited_2 or node2==-1):
                break
        
        return -1


                


