from itertools import accumulate
class Solution:
    breakpoints = [0]
    joined = None
    def encode(self, strs: List[str]) -> str:
        Solution.breakpoints += [*accumulate([len(s) for s in strs])]
        print(Solution.breakpoints)
        joined = ''.join(strs)
        return joined

    def decode(self, s: str) -> List[str]:
        res = [s[l:r] for l,r in zip(Solution.breakpoints[:-1],Solution.breakpoints[1:])]
        Solution.breakpoints = [0]
        Solution.joined = None
        return res