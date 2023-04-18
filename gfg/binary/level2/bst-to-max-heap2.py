class Node:
    def __init__(self) -> None:
        self.data = 0
        self.left=None 
        self.right = None 

# Helper function that allocates a new node 
# with the given data and None left and right 
# pointers

def getNode(data):
    newNode = Node()
    newNode.data = data
    newNode.left = newNode.right = None
    return newNode

# to find parent index
def paren(i):
    return (i-1)//2 

# heapify_up to arrange like max-heap 

def heapify_up(q,i):
    while i>0 and q[paren(i)].data < q[i].data:
        q[paren(i)],q[i] = q[i], q[paren(i)]
        i=paren(i)

def convertToMaxHeapUtil(root):
    if root is None:
        return root
    
    # creating list for BST nodes 
    q = []
    q.append(root)
    i=0
    while len(q)!=i:
        if q[i].left is not None:
            q.append(q[i].left)
        if q[i].right is not None:
            q.append(q[i].right)
        i+=1 
    # calling root as max value in heap 
    root = q[0]
    i=0
    # updating left and right nodes of BST using list
    while i < len(q):
        if 2*i + 1 < len(q):
            q[i].left = q[2*i+1]
        else:
            q[i].left = None
        
        if 2*i+2 < len(q):
            q[i].right  = q[2*i+2]
        else:
            q[i].right = None
    return root

# Function to print postorder travversal of the tree

def postorderTraversal(root):
    if (root==None):
        return 
    
    # recur on left subtree 
    postorderTraversal(root.left)
    # then recur on right subtree 
    postorderTraversal(root.right)
    # print the root's data 
    print(root.data, end=" ")

    