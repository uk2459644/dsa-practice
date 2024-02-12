class Solution:
    def tribonacci(self,n:int)->int:
        if n==0:
            return 0
        if n==1 or n==2:
            return 1
        nli=[0]*(n+2)
        nli[0]=0
        nli[1]=1
        nli[2]=1
        for i in range(3,n+1):
            nli[i]=nli[i-1]+nli[i-2]+nli[i-3]
        
        return nli[n]
    