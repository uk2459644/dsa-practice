from collections import deque

class TreeNode:
    def __init__(self,val=0,left=None,right=None):
        self.val=val
        self.left=left
        self.right=right

class Solution:
    def maxLevelSum(self,root:TreeNode):
        mx=root.val
        level=1
        ans=1
        queue=deque([root])

        while queue:
            curSum=0
            for _ in range(len(queue)):
                node=queue.popleft()
                curSum+=node.val
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            
            if curSum > mx:
                ans=level
                mx=curSum
            level+=1
        
        return ans



