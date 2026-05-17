class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groups = {}
        for i,s in enumerate(strs):
            chars = frozenset({c: s.count(c) for c in set(s)}.items())
            if not chars in groups:
                groups[chars] = [i]
            else:
                groups[chars].append(i)
        
        res = []
        for group in groups.values():
            res.append(list(map(lambda x:strs[x],group)))
        
        return res



        