
class TreeNode:
    def __init__(self,val=0,left=None,right=None):
        self.val=val
        self.left=left
        self.right=right


first=None

def count(node):
    nonlocal first
    total=0
    if node:
        if node.val==x:
            first=node
        
        total+=count(node.left)+count(node.right)+1
    
    return total

s=count(root)
l=count(first.left)
r=count(first.right)
p=s-l-r-1

return l+r<p or l+p<r or r+p<l



