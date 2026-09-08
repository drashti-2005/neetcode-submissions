class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        group={}
        for s in strs:
            freq={}
            for ch in s:
                freq[ch]=freq.get(ch,0)+1
            key=tuple(sorted(freq.items()))
            if key not in group:
                group[key]=[]
            group[key].append(s)
        return list(group.values())

            
