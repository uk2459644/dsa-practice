
class Solution:
    def spiralOrder(self,matrix:list[list]):
        row=len(matrix)
        col=len(matrix[0])

        left=0
        right=col-1
        top=0
        bottom=row-1
        ans=[]

        while len(ans)<row*col:
            for i in range(left,right+1):
                ans.append(matrix[top][i])
            top+=1
            for i in range(top,bottom+1):
                ans.append(matrix[i][right])
            right-=1
            if top<=bottom:
                for i in range(right,left-1,-1):
                    ans.append(matrix[bottom][i])
                bottom-=1
            
            if left<=right:
                for i in range(bottom,top-1,-1):
                    ans.append(matrix[i][left])
                left+=1
        
        return ans






