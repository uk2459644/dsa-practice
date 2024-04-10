
class Solution:
    def goodDaysToRobBank(self,security:list[int],time:int):
        n=len(security)

        if time>n//2:
            return []
        
        inc=[0]*n
        for i in range(1,n):
            if security[i-1]>=security[i]:
                inc[i]=inc[i-1]+1
        
        dec=[0]*n
        for i in range(n-2,-1,-1):
            if security[i+1]>=security[i]:
                dec[i]=dec[i+1]+1
        
        ans=[]
        for i in range(n):
            if inc[i]>=time and dec[i]>=time:
                ans.append(i)
            
        return ans


