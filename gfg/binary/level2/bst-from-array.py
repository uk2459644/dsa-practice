# Python implementation to construct a Binary tree from
# parent array 

# a node structure 
class Node:
    # a utility function to create a new node
    def __init__(self,key) -> None:
        self.key = key 
        self.left = None 
        self.right = None 

"""
Creates a node with key as 'i'. If i is root, then
it changes root. If a parent of i is not created, then
it creates parent first.
"""
def createNode(parent,i,created, root):
    # if this node is already created
    if created[i] is not None:
        return 
    # created a new node and set created[i]
    created[i] = Node(i)
    # if 'i' is root, change root pointer and return
    if parent[i]==-1:
        root[0]==created[i]
        return 
    # if parent is not created, then create parent first
    if created[parent[i]] is None:
        createNode(parent, parent[i], created, root)
    
    # Find parent container
    p=created[parent[i]]
    # if this is first child of parent
    if p.left is None:
        p.left = created[i]
    # if second child 
    else:
        p.right = created[i]

# Creates tree from parent and returns root of the
# created tree 

def createTree(parent):
    n=len(parent)
    # create and array created[] to keep track
    # of created nodes, initialize all entries as Node
    created = [None for i in range(n+1)]
    root = [None]
    for i in range(n):
        createNode(parent,i,created,root)
    
    return root[0]

# Inorder traversal of tree 
def inorder(root):
    if root is not None:
        inorder(root.left)
        print(root.key, end=" ")
        inorder(root.right)
        