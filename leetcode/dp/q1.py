class Solution:
     
    def getMaximumGenerated(self, n: int) -> int:
        if n==0:
            return 0
        if n==1:
            return 1
        nli=[0]*(n+2)
        nli[0]=0
        nli[1]=1
        for i in range(2,n):
            j=i//2
            if i%2==0:
                nli[i]=nli[j]
            else:
                nli[i]=nli[j]+nli[j+1]
        
        return max(nli)
