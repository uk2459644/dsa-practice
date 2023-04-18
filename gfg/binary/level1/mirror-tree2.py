# Convert binary tree to its mirror

class newNode:
    def __init__(self,data) -> None:
        self.data = data 
        self.left = None 
        self.right = None
    
def mirror(root):
    if (root == None):
        return 
    
    q=[]
    q.append(root)
    # Do BFS, while doing BFS, keep swapping
    # left and right children

    while(len(q)):
        curr = q[0]
        q.pop(0)
        # swap left child with right child
        curr.left, curr.right = curr.right, curr.left 
        # append left and right children
        if (curr.left):
            q.append(curr.left)
        if(curr.right):
            q.append(curr.right)

def inOrder(node):
    if (node == None):
        return
    inOrder(node.left)
    print(node.data, end=" ")
    inOrder(node.right)
    
