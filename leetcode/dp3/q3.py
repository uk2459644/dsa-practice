
class Solution:
    def maxArea(self,height:list[int])->int:
        n=len(height)
        l,r=0,n-1
        ans=0
        while l<r:
            if height[l]<height[r]:
                water=int(abs(r-l))*height[l]
                if water>ans:
                    ans=water
                l+=1
            else:
                water=int(abs(r-l))*height[r]
                if water>ans:
                    ans=water
                r-=1
        return ans
    

