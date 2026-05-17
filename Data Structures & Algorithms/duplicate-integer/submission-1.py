class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        s = set()
        for num in nums:
            print(num)
            if num in s:
                return True
            else:
                s.add(num)
            
        return False