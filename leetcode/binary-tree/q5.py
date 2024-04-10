
class TreeNode:
    def __init__(self,val=0,left=None,right=None):
        self.val=val
        self.left=left
        self.right=right


class Solution:
    def isCompleteTree(self,root:TreeNode):

        if not root:
            return True
        
        queue=[root]
        isLast=False

        while queue:
            node=queue.pop(0)
            if not node:
                isLast=True
                continue
            if isLast:
                return False
            queue.append(node.left)
            queue.append(node.right)
        
        return True


