class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        shortest_str_len = len(sorted(strs,key = len)[0])
        longest = ""
        for i,ch in enumerate(strs[0][:shortest_str_len]):
            if all(ch == other_strs[i] for other_strs in strs):
                longest += ch
            else:
                break
        return longest