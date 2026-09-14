class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(s)<len(t):
            return ""
        t_freq={}
        for ch in t:
            t_freq[ch]=t_freq.get(ch,0)+1
        win={}
        left=0
        have=0
        need=len(t_freq)
        result=""
        result_len=float("inf")

        for right in range(len(s)):
            ch=s[right]
            if ch in t_freq:
                win[ch]=win.get(ch,0)+1
                if win[ch]==t_freq[ch]:
                    have+=1
            while have==need:
                if (right-left+1)<result_len:
                    result_len=right-left+1
                    result=s[left:right+1]
                l_ch=s[left]
                if l_ch in t_freq:
                    win[l_ch]-=1
                    if win[l_ch]<t_freq[l_ch]:
                        have-=1
                left+=1
        return result

        

            
