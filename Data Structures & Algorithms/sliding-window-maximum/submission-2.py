class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        l=0
        q=deque()
        result=[]
        for right in range(len(nums)):
            while q and q[0]<l:
                q.popleft()
            while q and nums[q[-1]]<nums[right]:
                q.pop()
            q.append(right)
            if right-l+1==k:
                result.append(nums[q[0]])
                l+=1
        return result