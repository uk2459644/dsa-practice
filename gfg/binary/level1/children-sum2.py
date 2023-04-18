from queue import Queue

"""
Helper class that allocates a new node with
the given data and None left and right pointer
"""

class newNode:
    def __init__(self, data) -> None:
        self.data = data 
        self.left = None 
        self.right = None 

# Returns 1 if children sum property holds for the
# given node and both of its children

def isSumProperty(root):
    # Stores the nodes at each subsequent level
    q = Queue()
    q.put(root)
    q.put(None)
    while not q.empty():
        curr = q.get()
        if curr == None:
            # if there are more elements to the tree
            if not q.empty():
                q.put(None)
            continue
        # Initialize sum with default value as 0
        sum =0 
        # Calculate sum = node.left.data + node.right.data 
        if curr.left:
            q.put(curr.left)
            sum+= curr.left.data 
        if curr.right:
            q.put(curr.right)
            sum+=curr.right.data 
        if sum != curr.data and sum!=0:
            return 0
        return 1 
    

