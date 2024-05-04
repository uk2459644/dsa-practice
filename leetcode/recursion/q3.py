class Solution:
    def findTheWinner(self, n: int, k: int) -> int:
        lst=[(i+1) for i in range(n)]
        # print(lst)
        def dfs(k,lst,ind):
            if len(lst)==1:
                return lst[0]
            else:
                ind=(ind+k-1)%len(lst)
                lst.pop(ind)
                return dfs(k,lst,ind)
        
        return dfs(k,lst,0)