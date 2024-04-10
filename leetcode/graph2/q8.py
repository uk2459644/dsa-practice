class TreeNode:
    def __init__(self,val=0,left=None,right=None):
        self.val=val
        self.left=left
        self.right=right

class Solution:
    def bstFromPreorder(self,preorder:list[int]):
        if not preorder:
            return None
        
        root = TreeNode(preorder[0])
        stack = [root]

        for value in preorder[1:]:
            node = TreeNode(value)
            if value<stack[-1].val:
                stack[-1].left=node
            else:
                while stack and value > stack[-1].val:
                    last = stack.pop()
                last.right=node
            stack.append(node)
        
        return root




