class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        d = {}
        for c in s:
            d[c] = d.get(c,0) + 1 
        print(d)
        for c in t:
            if c in d:
                d[c] -=1
            else:
                return False
        print(d)
        for key in d.keys():
            if d[key] !=0:
                return False
        return True

        