
class Solution:
    def smallestSubsequence(self,s:str):
        stack,dict1=[],{j:i for i,j in enumerate(s)}

        for i,j in enumerate(s):
            if j in stack:
                continue

            while stack and stack[-1]>j and dict1[stack[-1]]>i:
                stack.pop()
            
            stack.append(j)
        
        return "".join(stack)
    



