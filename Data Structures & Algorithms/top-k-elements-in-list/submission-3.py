class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq={}
        r=[]
        for num in nums:
            freq[num]=freq.get(num,0)+1
        
        while k>0:
            maximum = 0
            max_num = 0

            for num in freq:
                if freq[num] > maximum:
                    maximum = freq[num]
                    max_num = num

            r.append(max_num)
            del freq[max_num]

            k -= 1
        return r  