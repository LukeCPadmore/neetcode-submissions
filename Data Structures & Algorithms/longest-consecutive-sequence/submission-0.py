class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        s = set(nums)
        longest = 0
        for num in nums:
            curr_length = 0
            curr_num = num
            # Not start of a sequence
            if curr_num - 1 in s:
                continue
            while curr_num in s:
                curr_num += 1
                curr_length += 1
            longest = max(longest,curr_length)
        
        return longest

            
        