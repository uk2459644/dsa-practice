# program for printing vertical order of a given binary

# structure for a binary tree node 
class Node:
    def __init__(self, key) -> None:
        self.key = key 
        self.left = None 
        self.right = None 

# A function to create a new node 
def newNode(key):
    node = Node(key)
    return node

# Function to print vertical order of a binary
# tree with given root 
def printVerticalOrder(root):
    if not root:
        return 
    # Create a dictionary and store vertical 
    # order in dictionary using function 
    # getVerticalOrder()
    m={}
    hd=0
    # Create queue to do level order traversal 
    # Every item of queue contains node 
    # and horizontal distance
    q=[]
    q.append((root,hd))
    # mn and mx contain minimum and maximum horizontal
    # distance from root 
    mn,mx = 0,0
    while q:
        # pop from queue front 
        temp = q.pop(0)
        hd = temp[1]
        node = temp[0]
        # insert this node's data in 
        # vector of hash 
        if hd in m:
            m[hd].append(node.key)
        else:
            m[hd]=[node.key]
        
        if node.left:
            q.append((node.left,hd-1))
        if node.right:
            q.append((node.right,hd+1))
        
        # update mn and mx 
        if mn> hd:
            mn = hd
        elif mx < hd:
            mx = hd 
    # run the loop from minimum to maximum 
    # every horizontal distance hd 
    for i in range(mn,mx+1):
        for i in m:
            tmp = m[i]
            for j in range(len(tmp)):
                print(tmp[j], end=" ")
            print()


