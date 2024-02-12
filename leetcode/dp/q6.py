class Solution:
    def pascal(self,lis:list,k:int)->list:
        res=[0]*(k+1)
        res[0]=1
        res[k]=1
        for i in range(1,len(res)-1):
            res[i]=lis[i-1]+lis[i]
        return res
    
    def getRow(self,rowIndex:int)-> list[int]:
        prev=[1]
        for i in range(rowIndex):
            prev=Solution.pascal(self,prev,i+1)

        return prev
    