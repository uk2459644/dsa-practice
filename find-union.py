class DSU:
    # constructor
    def __init__(self,n) -> None:
        # declaring two arrays to hold
        # inforamtion about parent and rank of each node & 
        # defining size of the arrays.
        # Initializing their values by is and 0s.
        self.parent=[i for i in range(n)]
        self.rank = [0 for i in range(n)]

        # for i in range(n):
        #      self.parent.add(i)
        #      self.rank.add(0)
        # Find function 
        def find(self,node):
            # if node is the parent of itself then
            # it is the leader of the tree.
            if(node==self.parent[node]):
                return node
            # Else, finding parent and also 
            # compressing the paths.
            self.parent[node]=self.find(self.parent[node])
            return self.parent[node]
        
        # Union function
        def union(self,u,v):
            # make u as a leader
            # of its tree
            u=self.find(u)
            # make v as a leader of its tree
            v=self.find(v)
            # if u and v are not equal, because if they are already in
            # same tree and it does not make 
            # sense to perform union operation
            if(u!=v):
                # checking tree with smaller depth/height
                if(self.rank[u]<self.rank[v]):
                    temp=u
                    u=v
                    v=temp
                self.parent[v]=u
                # if now ranks are eaqual
                # increasing rank of u
                if(self.rank[u]==self.rank[v]):
                    self.rank[u]=self.rank[u]+1
           