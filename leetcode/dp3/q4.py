class Solution:

    def isMatch(self,s:str,p:str)->bool:
        r,c=len(s),len(p)
        def solve(pr,pc):
            if pr==r and pc==c:
                return True
            if pr==r and pc!=c:
                return False
            if pc==c and pr!=r:
                return False
            
            if s[pr]==p[pc] or p[pc]=="?":
                solve(pr+1,pc+1)
            if p[pc]=="*":
                if pc+1==c:
                    return True
                else:
                    solve(pr+1,pc+1) and solve(pr+1,pc) and solve(pr,pc+1)
        
        return solve(0,0)
    

