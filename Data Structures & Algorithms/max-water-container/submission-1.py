class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l=0
        r=len(heights)-1
        maximum=0
        while l<r:
            width=r-l
            minimum=min(heights[l],heights[r])
            score=width*minimum
            if heights[l]<heights[r]:
                l+=1
            else:
                r-=1  
            maximum=max(score,maximum) 
        return maximum