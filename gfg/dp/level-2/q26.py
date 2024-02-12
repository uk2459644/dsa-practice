# Method 1 dynamic programming using tabulation

# Generate all 3 rotations of all boxes. The size of rotation array becomes 3 times
# the size of the original array. For simplicity, we consider width as always smaller than
# or equal to depth

# Dynamic programming implementation of Box stacking problem

class Box:
    # Representation of a box
    def __init__(self,h,w,d) -> None:
        self.h=h
        self.w=w
        self.d=d

    def __lt__(self,other):
        return self.d*self.w< other.d*other.w
    
def maxStackHeight(arr,n):
    # Create an array of all rotations of given boxes. For example,
    # for a box(1,2,3), we coonsider three instances {{1,2,3},{2,1,3},{3,1,2}}
    rot=[Box(0,0,0) for _ in range(3*n)]
    index=0

    for i in range(n):
        # copy the original box
        rot[index].h=arr[i].h
        rot[index].d=max(arr[i].d,arr[i].w)
        rot[index].w=min(arr[i].d,arr[i].w)

        index+=1

        # First rotation of the box
        rot[index].h=arr[i].w
        rot[index].d=max(arr[i].h,arr[i].d)
        rot[index].w=max(arr[i].h,arr[i].d)
        index+=1 
        # Second rotation of the box
        rot[index].h=arr[i].d
        rot[index].d=max(arr[i].h,arr[i].w)
        rot[index].w=max(arr[i].h,arr[i].w)
        index+=1 
    
    # Now the number of boxes is 3n
    n*=3 
    # Sort the array 'rot[]' in non-increasing order of base area
    rot.sort(reverse=True)
    # Uncomment followinng two lines to print all rotation
    # Initialize msh values for all indexes msh[i]--> MAximum possible stack
    # height with box i on top
    msh=[0]*n
    for i in range(n):
        msh[i]=rot[i].h
    
    # Compute optimized msh values in bottom up manner
    for i in range(1,n):
        for j in range(0,i):
            if (rot[i].w < rot[j].w and rot[i].d < rot[j].d):
                if msh[i] < msh[j]+rot[i].h:
                    msh[i]=msh[j]+rot[i].h
    
    maxm=-1
    for i in range(n):
        maxm=max(maxm,msh[i])

    return maxm
