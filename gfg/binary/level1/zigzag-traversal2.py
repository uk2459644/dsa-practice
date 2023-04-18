# code for recursive approach 
from collections import defaultdict 
from collections import deque 

class Node:
    def __init__(self,val) -> None:
        self.data = val
        self.left = None 
        self.right = None 

# function to build tree 
def buildTree(s):
    if (len(s)==0 or s[0]=="N"):
        return None 
    
    # creating list of strings from input
    # string after splitting by space 
    ip = list(map(str,s.split()))
    # create the root of the tree 
    root = Node(root)
    size =0 
    q = deque()
    q.append(root)
    size+=1 

    i=1 
    while (size>0 and i < len(ip)):
        currNode  = q[0]
        q.popleft()
        size = size-1 
        