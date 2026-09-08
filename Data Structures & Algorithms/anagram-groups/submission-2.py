class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        d={}

        for word in strs:
            freq={}
            for ch in word:
                freq[ch]=freq.get(ch,0)+1
            key=tuple(sorted(freq.items()))
            if key not in d:
                d[key]=[]
            d[key].append(word)
        return list(d.values())
            