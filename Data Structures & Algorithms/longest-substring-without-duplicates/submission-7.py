class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        chars = [0] * 128
        l = r = 0
        currMax = 0
        while r < len(s):
            chars[ord(s[r])] +=1
            while chars[ord(s[r])] > 1:
                chars[ord(s[l])] -= 1
                l+=1
            
            currMax = max(currMax,r-l+1)
            r+=1
        
        return currMax
                


        
        