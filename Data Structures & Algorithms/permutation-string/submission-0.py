class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False
        
        d1 = {c:s1.count(c) for c in set(s1)}
        d2 = {c:s2[:len(s1)].count(c) for c in set(s2[:len(s1)])}
        l,r = 0,len(s1) - 1

        while True:
            print(d1,d2)
            if d1 == d2:
                return True
            if d2[s2[l]] == 1:
                d2.pop(s2[l])
            else:
                d2[s2[l]] -=1
            l+=1
            r+=1
            if r == len(s2):
                break
            d2[s2[r]] = d2.get(s2[r],0) + 1

        return False
        