
import math

class TreeNode:
    def __init__(self,val=0,left=None,right=None):
        self.val=val
        self.left=left
        self.right=right

class Solution:
    def maxRowVal(self,root:TreeNode):
        if not root:
            return []
        
        ans=[]
        queue=[root]

        while queue:
            mx=-math.inf
            n=len(queue)
            for _ in range(n):
                node=queue.pop(0)
                mx=max(node.val,mx)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            
            ans.append(mx)
        
        return ans



