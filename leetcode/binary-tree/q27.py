# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

        
class Solution:
    def recoverTree(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        lst=[]
        def dfs(node):
            if node:
                dfs(node.left)
                lst.append(node.val)
                dfs(node.right)
        
        dfs(root)

        lst.sort()
        def dfs2(node,lst):
            if node:
                dfs2(node.left,lst)
                node.val=lst.pop(0)
                dfs2(node.right,lst)
        
        dfs2(root,lst)


        