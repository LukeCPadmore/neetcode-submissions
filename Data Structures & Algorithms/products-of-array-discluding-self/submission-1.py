import math
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix = []
        suffix = []
        for i in range(len(nums)):
            prefix.append(math.prod(nums[:i]) if i > 0 else 1)
            suffix.append(math.prod(nums[i+1:]) if i < len(nums) else 1)
        
        return [a*b for a,b in zip(prefix,suffix)]

        