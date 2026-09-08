class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l=0
        r=len(heights)-1
        maximum=0
        while l<r:
            width=r-l
            minimun=min(heights[l],heights[r])
            store=width*minimun
            maximum=max(maximum,store)
            if heights[l] < heights[r]:
                l += 1
            else:
                r -= 1
            
        return maximum
