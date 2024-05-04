
class Solution:
    def validStack(self,pushed:list[int],popped:list[int]):
        i=0
        stack=[]
        for nm in pushed:
            stack.append(nm)
            while stack and stack[-1]==popped[i]:
                stack.pop()
                i+=1
        
        return False if stack else True


