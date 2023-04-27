"""
Method 3: 
It uses the concept of hashing. the following steps are:
- Map the element of the 1st row in a hash table. Let it be hash.
- For row=2 to n
- map each element of the current row into a temporary hash table.
  let it be temp.
- Iterate through the elements of hash and check that the elements in
  hash are present in temp. If not present then delete those elements from
  hash.
- when all the rows are being processed in this manner, then the elements
left in hash are the required common elements.

"""
MAX=100

def findAndPrintCommonElements(mat,n):
    us=dict()

    for i in range(n):
        us[mat[0][i]]=1
    
    for i in range(1,n):
        temp=dict()

        for j in range(n):
            temp[mat[i][j]]=1
        # iterate through all the elements of us
        for itr in list(us):
            # if an element of 'us' is not present
            # into 'temp', then erase that element from 'us'
            if itr not in temp:
                del us[itr]
        
        # if size of 'us' becomes 0, then there are no common elements
        if len(us)==0:
            break
    
    for itr in list(us)[::-1]:
        print(itr,end=" ")
        
