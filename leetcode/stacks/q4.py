class Solution:
    def buildArray(self,target:list[int],n:int):
        lst=[(i+1) for i in range(n)]
        ans=[]
        seen=[]
        
        for nm in lst:
            if seen == target:
                break
            if nm in target:
                seen.append(nm)
                ans.append("Push")
            else:
                ans.append("Push")
                ans.append("Pop")
        
        return ans


