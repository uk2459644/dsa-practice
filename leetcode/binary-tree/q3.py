class TreeNode:
    def __init__(self,val=0,left=None,right=None):
        self.val=val
        self.left=left
        self.right=right


def find_node(root:TreeNode,key,parent):
    if root is None:
        return None,None
    
    if root.val==key:
        return root,parent
    
    left_node,left_parent=find_node(root.left,key,root)
    if left_node:
        return left_node,left_parent
    
    




