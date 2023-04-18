# python program to find diameter of a binary tree

class newNode:
    def __init__(self,data) -> None:
        self.data=data 
        self.left=self.right=None

# function to find height of a tree
def height(root,ans):
    if (root==None):
        return 0
    
    left_height=height(root.left,ans)
    right_height=height(root.right,ans)
    ans[0]=max(ans[0],1+left_height+right_height)

    return 1+max(left_height,right_height)

def diameter(root):
    if (root==None):
        return 0
    ans=[-999999999999]
    height_of_tree=height(root,ans)
