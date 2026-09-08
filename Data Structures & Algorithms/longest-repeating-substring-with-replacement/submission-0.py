class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        l=0
        max_length=0
        max_freq=0
        freq={}
        for right in range(len(s)):
            freq[s[right]]=freq.get(s[right],0)+1
            max_freq=max(max_freq,freq[s[right]])
            while (right-l+1)-max_freq>k:
                freq[s[l]]-=1
                l+=1
            max_length=max(max_length,right-l+1)
        return max_length
            
        