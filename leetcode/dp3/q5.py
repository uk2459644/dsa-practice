
class Solution:
    def isMatch(self,s:str,p:str)->bool:
        n,m=len(s),len(p)
        @__cached__
        def dp(i,j):
            if j == m:
                return i==n
            if i==n:
                return p[j:].count("*") == m-j
            
            if p[j]=="*":
                return dp(i,j+1) or dp(i+1,j)
            elif p[j]=="?":
                return dp(i+1,j+1)
            else:
                return s[i]==p[j] and dp(i+1,j+1)
        return dp(0,0)
