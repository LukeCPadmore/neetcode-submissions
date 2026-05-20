from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = []
        sorted_strs = [tuple(sorted(strs)) for strs in strs]
        d = defaultdict(list)
        for i,s in enumerate(sorted_strs):
            d[s].append(i)
        res = [[strs[idx] for idx in group] for group in d.values()]
        return res
        
        