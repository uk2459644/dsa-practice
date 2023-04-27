"""
Method 2: Using HashMap

This approach uses a hashmap instead of creating a hashtable of size
max element +1.
"""
def unique(mat,r,c)->int:
    mp={}
    for i in range(r):
        for j in range(c):
            if mat[i][j] not in mp:
                mp[(mat[i][j])]=1
            else:
                mp[(mat[i][j])]+=1 
    
    flag=False

    # print unique element
    for p in mp:
        if mp[p]==1:
            print(p)
            flag=True
    
    if flag==False:
        print("No unique element in the matrix")
        