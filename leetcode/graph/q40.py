from collections import deque


class TreeNode:
    def __init__(self,val=0,left=None,right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def deepestLeavesSum(self,root:TreeNode):
        queue = deque([root])
        backQueue = queue.copy()

        while queue:
            backQueue = queue.copy()
            for _ in range(len(queue)):
                node =  queue.popleft()
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
        
        return sum([node.val for node in backQueue])
        

