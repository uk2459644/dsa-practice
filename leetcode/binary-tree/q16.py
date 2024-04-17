
from collections import deque

class TreeNode:
    def __init__(self,val=0,left=None,right=None):
        self.val=val
        self.left=left
        self.right=right

class Solution:

    def addRow(self,root:TreeNode,val:int,depth:int):
        if depth==1:
            return TreeNode(val,left=root)
        
        queue=deque([root])
        level=1
        while level<depth-1:
            for _ in range(len(queue)):
                node=queue.popleft()

                if node.left:
                    queue.append(node.left)
                
                if node.right:
                    queue.append(node.right)
                
                level+=1
        
        for _ in range(len(queue)):
            node=queue.popleft()
            node.left=TreeNode(val,left=node.left)
            node.right=TreeNode(val,right=node.right)
        
        return root
        

        



