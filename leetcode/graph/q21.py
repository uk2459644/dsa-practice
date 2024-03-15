class TreeNode:
    def __init__(self,val=0,left=None,right=None):
        self.val=val
        self.left=left
        self.right=right

parents = [-1,2,0,2,0]

n=len(parents)

tree={}
for i in range(n):
    if i==0:
        node=TreeNode(i)
        tree[i]=node
    else:
        parent=parents[i]
        if parent not in tree.keys():
            node=TreeNode(parent)
            tree[parent]=node
            if i not in tree.keys():
                node.left=TreeNode(i)
                tree[i]=node.left
            else:
                node.left=tree[i]
        else:
            node=tree[parent]
            if node.right:
                node.left=TreeNode(i)
                tree[i]=node.left
            else:
                node.right=TreeNode(i)
                tree[i]=node.right

root=tree[0]

def dfs(root:TreeNode):
    print(root.val)
    if root.left:
        dfs(root.left)
    if root.right:
        dfs(root.right)
    

dfs(root)





