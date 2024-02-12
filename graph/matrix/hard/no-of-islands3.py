"""
No of islands using disjoint set data structure. The idea is to consider all 1 values
as individual sets. Traverse the matrix and do a union of all adjacent 1 vertices.

Below are detailed steps:
1. Initialize the result (count of islands) as 0
2. Traverse each index of the 2D matrix
3. If the value at that index is 1, check all its 8 neighbours. If a neighbour
   is also equal to 1, take the union of the index and its neighbour.

4. Now define an array of sixe row*column to store frequencies of all sets.
5. Now traverse the matrix again.
6. If the value at the index is 1, find its set.
7. If the frequency of the set in the above array is 0,
   increment the result by 1.
"""
class DisjointUnionSets:
    def __init__(self,n) -> None:
        self.rank=[0]*n
        self.parent=[0]*n
        self.n=n
        self.makeSet()
       
    def makeSet(self):
        # initially, all elements are in their own set
        for i in range(self.n):
            self.parent[i]=i
    
    # find the representative of the set that x is an element of
    def find(self,x):
        if (self.parent[x]!=x):
            # if x is not the parent of itself, then x is not the representative
            # of its set. so we recursively call find on its parent and move i's node
            # directly under the representative of this set
            self.parent[x]=self.find(self.parent[x])
        
        return self.parent[x]
    
    # unites the set that includes x and the set that includes y
    def Union(self,x,y):
        # find the representatives (or the root nodes) for x and y
        xRoot = self.find(x)
        yRoot = self.find(y)
        # Elements are in the same set, no need to unite anything
        if xRoot==yRoot:
            return
        # If x's rank is less than y's rank then move x under y so that 
        # depth of tree remains less
        if self.rank[xRoot] < self.rank[yRoot]:
            self.parent[xRoot]=yRoot
        elif self.rank[yRoot] < self.rank[xRoot]:
            self.parent[yRoot]=xRoot
        else:
            self.parent[yRoot]=xRoot
            # and increment the result tree's rank by 1
            self.rank[xRoot]=self.rank[xRoot]+1
    
    
        

