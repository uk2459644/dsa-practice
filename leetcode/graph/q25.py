from collections import deque

class TreeNode:
    def __init__(self,val=0,left=None,right=None):
        self.val=val
        self.left=left
        self.right=right

class Solution:

    def delNodes(self,root:TreeNode,to_delete:list[int]):
        ans=list()

        del_set = set(to_delete)
        queue=deque()
        queue.append((root,True))

        while queue:
            node,is_root=queue.popleft()
            can_delete = node.val in del_set
            if is_root and not can_delete:
                ans.append(node)
            if node.left:
                queue.append(node.left,can_delete)
            if node.right:
                queue.append(node.right,can_delete)
        
        return ans

            





