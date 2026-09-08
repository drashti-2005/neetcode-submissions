class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        s_len=len(s1)
        if len(s1) > len(s2):
            return False
        s_freq={}
        for ch in s1:
            s_freq[ch]=s_freq.get(ch,0)+1
        win_freq = {}
        for i in range(s_len):
            win_freq[s2[i]] = win_freq.get(s2[i], 0) + 1

        if win_freq == s_freq:
            return True
        for right in range(s_len,len(s2)):
            win_freq[s2[right]]=win_freq.get(s2[right],0)+1 
            
            left=right-s_len
            win_freq[s2[left]]-=1
            
            if win_freq[s2[left]]==0:
                del win_freq[s2[left]]
            if win_freq==s_freq:
                return True
        return False

