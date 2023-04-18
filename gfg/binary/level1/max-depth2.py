# max-depth by level order approach
# a tree node

class Node:
    def __init__(self) -> None:
        self.key =0
        self.left, self.right = None, None

# utility function to create a new node

def newNode(key):
    temp= Node()
    temp.key = key
    temp.left, temp.right = None, None

# function to find the height(depth) of the tree

def height(root):
    # Initialising a variable to count the
    # tree
    depth = 0
    q=[]
    # appending first level element along with None
    q.append(root)
    q.append(None)
    while (len(q)>0):
        temp = q[0]
        q=q[1:]
        # When None encountered, increment the value
        if(temp == None):
            depth+=1
        
        # If none not encountered, keep moving
        if(temp!=None):
            if(temp.left):
                q.append(temp.left)
            if (temp.right):
                q.append(temp.right)
        
        # if queue still have elements left
        # append None again to the queue
        elif(len(q)>0):
            q.append(None)
    
    return depth

root =  newNode(1)
root.left = newNode(2)
root.right = newNode(3)

root.left.left = newNode(4)
root.left.right = newNode(5)

print(f"Height (Depth) of tree is: {height(root)}")

