
from collections import deque

class TreeNode:
    def __init__(self,val=0,left=None,right=None):
        self.val=val
        self.left=left
        self.right=right


class Solution:
    def bottomLeftLeave(self,root:TreeNode):
        ans=0
        queue=deque([root])

        while queue:
            node=queue.popleft()
            ans=node.val
            if node.right:
                queue.append(node.right)
            if node.left:
                queue.append(node.left)

        return ans
                





