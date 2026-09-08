class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack=[]
        max_a=0
        for i in range(len(heights)):
            while stack and heights[i]<heights[stack[-1]]:
                h=heights[stack.pop()]
                if stack:
                    width=i-stack[-1]-1
                else:
                    width=i
                a=h*width
                max_a=max(max_a,a)
            stack.append(i)
        n=len(heights)
        while stack:
            h=heights[stack.pop()]
            if stack:
                width=n-stack[-1]-1
            else:
                width=n
            a=h*width
            max_a=max(max_a,a)
        return max_a