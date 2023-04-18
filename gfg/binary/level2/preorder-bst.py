# Program for an efficient solution to check if a 
# given array can represent preorder traversal of a 
# binary search tree 

INT_MIN = -2**32

def canRepresentBST(pre):
    # Create an empty stack
    s=[]
    # Initialize current root as minimum possible value
    root = INT_MIN 
    # Traverse given array 
    for value in pre:
        # Note value is equal to pre[i] according to the 
        # given algo 
        # If we find a node who is on the right side 
        # and smaller than root, return False 
        if value < root:
            return False
        # If value(pre[i]) is in right subtree of stack top,
        # Keep removing items smaller than value and 
        # make the last removed items as new root
        while (len(s) > 0 and s[-1]<value):
            root = s.pop()
        # At this point either stack is empty or value
        # is smaller than root, push value 
        s.append(value)
    return True
