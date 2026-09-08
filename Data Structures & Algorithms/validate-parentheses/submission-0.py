class Solution:
    def isValid(self, s: str) -> bool:
        pair={
            ")":"(",
            "}":"{",
            "]":"["
            }
        r=[]
        for ch in s:
            if ch in "({[":
                r.append(ch)
            elif ch in ")}]" :
                if not r or r[-1]!=pair[ch]:
                    return False
                r.pop()
        return len(r)==0

                