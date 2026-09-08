class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq={}
        ans=[]
        for num in nums:
            freq[num]=freq.get(num,0)+1
        d=dict(sorted(freq.items(),key=lambda x:x[1],reverse=True))
        for num in d:
            if len(ans)==k:
                break
            ans.append(num)
        return ans
