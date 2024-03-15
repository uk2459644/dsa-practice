
class Solution:
    def findCircleNum(self,isConnected:list[list[int]])->int:
        # Initialize visited set
        visited=set()

        # Define depth-first search (dfs) function
        def dfs(isConnected,visited,i):
            if i in visited:
                return 0
            
            visited.add(i)
            for j in range(len(isConnected[i])):
                if isConnected[i][j]==1:
                    dfs(isConnected,visited,j)
            
            return 1
        
        provinces=0
        # Initialize provinces count
        for i in range(len(isConnected)):
            provinces+=dfs(isConnected,visited,i)
        return provinces


